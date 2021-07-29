import datetime

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask import flash, redirect, render_template, request, url_for  #, g
from flask_babel import lazy_gettext as _l, get_locale
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

import climsoft
from climsoft import forms
from climsoft.models import FormSynoptic2Ra1, Obselement, Station


# Temporarily used to allow the base.html template to render correctly
BASE_VARS = {
    'user': {'is_authenticated': True},
    'settings': {'CUSTOM_THEME': ''},
}


def get_or_create(session, model, **kwargs):
    # a/6078058
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


#@app.before_request
#def before_request():
##    if current_user.is_authenticated:
##        current_user.last_seen = datetime.utcnow()
##        db.session.commit()
#    g.locale = str(get_locale())


@app.route('/')
@login_required
def index():
    return render_template('index.html', **BASE_VARS)


@app.route('/user_admin/')
@login_required
def user_admin():
    return render_template('user_admin.html', **BASE_VARS)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_l('Invalid username or password'))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # netloc is used to ensure the user is not redirected to another domain
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    # Currently not using the 'title' variable in base.html
    databases = app.config['SQLALCHEMY_BINDS'].keys()
    return render_template(
        'login.html', title=_l('Sign In'), form=form, databases=databases, **BASE_VARS)


###@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_l('Congratulations, you are now a registered user!'))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form, **BASE_VARS)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))


# ---------------------------
# Metadata management

@app.route('/metadata/')
def metadata():
    return render_template('metadata/metadata.html', **BASE_VARS)


@app.route('/metadata/station/<station_id>/')
def station(station_id):
    Station = climsoft.models.Station
    station = Station.query.get_or_404(station_id)
    form = forms.StationForm(obj=station)
    return render_template('metadata/station_form.html', form=form, **BASE_VARS)


@app.route('/metadata/element/<element_id>/')
def element(element_id):
    Obselement = climsoft.models.Obselement
    element = Obselement.query.get_or_404(element_id)
    form = forms.ObselementForm(obj=element)
    return render_template('metadata/obselement_form.html', form=form, **BASE_VARS)


@app.route('/metadata/station/select/')
def station_select():
    options = ""
    for station in Station.query.order_by(Station.stationName):
        options += "<option value='{}'>{}</option>".format(
            station.stationId, station.stationName
        )
    return options


@app.route('/metadata/element/select/')
def element_select():
    options = ""
    for element in Obselement.query.order_by(Obselement.elementName):
        options += "<option value='{}'>{}</option>".format(
            element.elementId, element.elementName
        )
    return options


'''
    path('station/', views.MetadataList.as_view(model=models.Station), name='station-index'),
    path('station/select/', name='station-select', view = views.MetadataList.as_view(
        model=models.Station, template_name='metadata/station-select.html', order_by='stationname')),
    path('station/create/', views.MetadataCreate.as_view(model=models.Station), name='station-create'),  # FIXME: defaults to template_name = metadata/station_form.html without model form
    path('station/<pk>/', name='station-read', view=views.MetadataRead.as_view(
        model=models.Station, form_class=forms.StationForm, template_name='metadata/station_form.html'
    )),
    path('station/<pk>/update/', views.MetadataUpdate.as_view(), name='station-update'),
    path('station/<pk>/delete/', views.MetadataDelete.as_view(), name='station-delete'),
'''


# ---------------------------
# Key entry

@app.route('/keyentry/')
@login_required
def keyentry():
    return render_template('keyentry/keyentry.html', **BASE_VARS)


@app.route('/keyentry/synoptic2ra1/')
def form_synoptic2ra1():
    # TODO: selector should be populated from application db user table or default to today's date
    now = datetime.datetime.now()
    vars = {
        'station_id': 67775050,  # FIXME: hardcoded default for climsoft test database
        'year': now.year,
        'month': now.month,
        'day': now.day,
        'hour': now.hour,
    }
    return redirect('/keyentry/synoptic2ra1/{station_id}/{year}/{month}/{day}/{hour}'.format(**vars))

@app.route('/keyentry/synoptic2ra1/<station_id>/<year>/<month>/<day>/<hour>/')
def form_synoptic2ra1_selector(station_id, year, month, day, hour):
    # FIXME: try on int conversion
    pk = {
        'stationId': 1,#station_id,
        'yyyy': int(year),
        'mm': int(month),
        'dd': int(day),
        'hh': int(hour),
    }
    form, form_name = None, 'synoptic2ra1'
    
    if not Station.query.filter_by(stationId=station_id).count():
        flash('Station not found', 'halt')
    else:
        model = climsoft.models.FormSynoptic2Ra1
        obj = get_or_create(db.session, model, **pk)
        form = climsoft.forms.Synoptic2Ra1Form(obj=obj)

    return render_template(
        'keyentry/keyentry_form.html',
        form=form,
        form_name=form_name,
        vars = {'station_id': station_id, 'year': year, 'month': month, 'day': day, 'hour': hour,},
        **BASE_VARS,
    )


@app.route('/keyentry/hourly/')
def form_hourly():
    # TODO: selector should be populated from application db user table or default to today's date
    now = datetime.datetime.now()
    vars = {
        'station_id': 67775050,  # FIXME: hardcoded default for climsoft test database
        'element_id': 2,  # FIXME: hardcoded default element
        'year': now.year,
        'month': now.month,
        'day': now.day,
    }
    return redirect('/keyentry/hourly/{station_id}/{element_id}/{year}/{month}/{day}'.format(**vars))

@app.route('/keyentry/hourly/<station_id>/<element_id>/<year>/<month>/<day>/')
def form_hourly_selector(station_id, element_id, year, month, day):
    form = forms.ObselementForm(obj=element)
    return render_template(
        'keyentry/keyentry_form.html',
        form=form,
        form_name='hourly',
        vars = {'station_id': station_id, 'element_id': element_id,
            'year': year, 'month': month, 'day': day,
        },
        **BASE_VARS,
    )


@app.route('/keyentry/daily2/')
def form_daily2():
    # TODO: selector should be populated from application db user table or default to today's date
    now = datetime.datetime.now()
    vars = {
        'station_id': 67775050,  # FIXME: hardcoded default for climsoft test database
        'element_id': 2,  # FIXME: hardcoded default element
        'year': now.year,
        'month': now.month,
        'hour': now.hour,
    }
    return redirect('/keyentry/daily2/{station_id}/{element_id}/{year}/{month}/{hour}'.format(**vars))

@app.route('/keyentry/daily2/<station_id>/<element_id>/<year>/<month>/<hour>/')
def form_daily2_selector(station_id, element_id, year, month, hour):
    form = forms.ObselementForm(obj=element)
    return render_template(
        'keyentry/keyentry_form.html',
        form=form,
        form_name='daily2',
        vars = {'station_id': station_id, 'element_id': element_id,
                'year': year, 'month': month, 'hour': hour,
        },
        **BASE_VARS,
    )


@app.route('/keyentry/monthly/')
def form_monthly():
    # TODO: selector should be populated from application db user table or default to today's date
    now = datetime.datetime.now()
    vars = {
        'station_id': 67775050,  # FIXME: hardcoded default for climsoft test database
        'element_id': 2,  # FIXME: hardcoded default element
        'year': now.year,
    }
    return redirect('/keyentry/monthly/{station_id}/{element_id}/{year}'.format(**vars))

@app.route('/keyentry/monthly/<station_id>/<element_id>/<year>/')
def form_monthly_selector(station_id, element_id, year):
    form = forms.ObselementForm(obj=element)
    return render_template(
        'keyentry/keyentry_form.html',
        form=form,
        form_name='monthly',
        vars = {'station_id': station_id, 'element_id': element_id, 'year': year},
        **BASE_VARS,
    )


'''
HOURLY = {
    'model': 'FormHourly',
    'name': 'hourly',
    'reverse': 'keyentry:form_hourly',
    'selector': 'keyentry/selector_hourly.html',
    'title': 'Hourly Data',
}

DAILY2 = {
    'model': 'FormDaily2',
    'name': 'daily2',
    'reverse': 'keyentry:form_daily2',
    'selector': 'keyentry/selector_daily2.html',
    'title': 'Daily data for the whole month',
}

MONTHLY = {
    'model': 'FormMonthly',
    'name': 'monthly',
    'reverse': 'keyentry:form_monthly',
    'selector': 'keyentry/selector_monthly.html',
    'title': 'Monthly Data',
}

SYNOPTIC2RA1 = {
    'model': 'FormSynoptic2Ra1',
    'name': 'synoptic2ra1',
    'reverse': 'keyentry:form_synoptic2ra1',
    'selector': 'keyentry/selector_synoptic2ra1.html',
    'title': 'Synoptic data for input into TCDF form for RA1',
}


urlpatterns = [
    path('', views.ContentsView.as_view(), name='contents'),
    path('hourly/', views.KeyEntryView.as_view(extra_context=HOURLY), name='form_hourly'),
    path('daily2/', views.KeyEntryView.as_view(extra_context=DAILY2), name='form_daily2'),
    path('monthly/', views.KeyEntryView.as_view(extra_context=MONTHLY), name='form_monthly'),
    path('synoptic2ra1/', views.KeyEntryView.as_view(extra_context=SYNOPTIC2RA1), name='form_synoptic2ra1'),

    path('hourly/<pk>/update/', name='hourly-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormHourly, form_class=forms.HourlyForm, template_name='keyentry/formhourly_form.html')),
    path('daily2/<pk>/update/', name='daily2-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormDaily2, form_class=forms.Daily2Form, template_name='keyentry/formdaily2_form.html')),
    path('monthly/<pk>/update/', name='monthly-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormMonthly, form_class=forms.MonthlyForm, template_name='keyentry/formmonthly_form.html')),
    path('synoptic2ra1/<pk>/update/', name='synoptic2ra1-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormSynoptic2Ra1, form_class=forms.Synoptic2Ra1Form, template_name='keyentry/formsynoptic2ra1_form.html')),
]
'''