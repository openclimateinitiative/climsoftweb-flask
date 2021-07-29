from collections import namedtuple

from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory

from app import db
from climsoft import models


ValueFlag = namedtuple('ValueFlag', 'value flag')


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

    def __init__(self, *args, **kwargs):
        """ Allow labels to be set in a dictionary in meta (Django-style) """
        super(ModelForm, self).__init__(*args, **kwargs)
        for field, label in self.Meta.labels.items():
            f = getattr(self, field)
            f.label.text = label


# _____________________________

class StationForm(ModelForm):
    class Meta:
        model = models.Station
        labels = {
            'stationId': _l('Station Id'),
            'stationName': _l('Station Name'),
            'wmoid': _l('WMO Id'),
            'icaoid': _l('ICAO Id'),
            'latitude': _l('Latitude'),
            'qualifier': _l('Qualifier'),
            'longitude': _l('Longitude'),
            'elevation': _l('Elevation'),
            'geoLocationMethod': _l('Geographical Method'),
            'geoLocationAccuracy': _l('Geographical Accuracy'),
            'openingDatetime': _l('Opening Date'),
            'closingDatetime': _l('Closing Date'),
            'country': _l('Country'),
            'authority': _l('Authority'),
            'adminRegion': _l('Admin Region'),
            'drainageBasin': _l('Drainage Basin'),
            #'wacaSelection': '',
            #'cptSelection': '',
            'stationOperational': _l('Station Operational'),
        }
        include = labels.keys()


class ObselementForm(ModelForm):
    class Meta:
        model = models.Obselement
        labels = {
            'elementId': _l('ID'),
            'abbreviation': _l('Abbreviation'),
            'elementName': _l('Name'),
            'description': _l('Description'),
            'elementScale': _l('Scale'),
            'upperLimit': _l('Upper Limit'),
            'lowerLimit': _l('Lower Limit'),
            'units': _l('Unit'),
            'elementtype': _l('Type'),
            'qcTotalRequired': _l('Total Required'),
            'selected': _l('Selected'),
        }
        include = labels.keys()


class Synoptic2Ra1Form(ModelForm):
    COLUMNS = (
        ('106', '107', '400', '814', '399', '301', '185', '101', '102', '103', '105', '110', '192', '114', '115', '168', '169', '170', '171',),
        ('119', '116', '117', '118', '123', '120', '121', '122', '127', '124', '125', '126', '131', '128', '129', '130',),
        ('167', '197', '193', '002', '003', '099', '018', '084', '132', '005', '174', '112', '111',),
    )

    class Meta:
        # TODO: missing signature and entryDatetime
        model = models.FormSynoptic2Ra1
        labels = {
            'stationId': 'Station:',
            'yyyy': 'Year:',
            'mm': 'Month:',
            'dd': 'Day:',
            'hh': 'Hour:',

            'Val_Elem106': 'Station Level Pressure-Po',  # Pressure  Station
            'Val_Elem107': 'Pressure Reduced to MSL-P',  # Pressure  Sea Level
            'Val_Elem400': '3hr Pessure Change-P3',  # 3 Hr Pressure Change
            'Val_Elem814': '3hr Pressure Characteristic',  # 3Hr Pressure Characteristic
            'Val_Elem399': '24hr Pessure Change-P24',  # Press Tendancy  24 Hly
            'Val_Elem301': 'Standard Pressure Level -a',  # Pressure Level
            'Val_Elem185': 'Geopotential Height-hhh',  # Pressure  GPM
            'Val_Elem101': 'DryBulb Temp-TTT',  # Temp  Dry Bulb
            'Val_Elem102': 'Wetbulb Temp-TwTwTw',  # Temp  Wet Bulb
            'Val_Elem103': 'DewPoint Temp-TdTdTd',  # Temp  Dew Point
            'Val_Elem105': 'Relative Humidity-U',  # Relative Humidty 06Z
            'Val_Elem110': 'Horizontal Visibility-VV',  # Visibility Hor
            'Val_Elem192': 'Low Cloud Hght-h',  # Cloud Height Lowest Lvl
            'Val_Elem114': 'Total Cloud Cover- N',  # Cloud Cover  total
            'Val_Elem115': 'Vertical Significance',  # Cloud Opacty tot
            'Val_Elem168': 'Low Lvl Clouds Amount-Nh',  # Cloud Amt Type Height Lvl1
            'Val_Elem169': 'Low Lvl Clouds Type-CL',  # Cloud Amt Type Height Lvl2
            'Val_Elem170': 'Medium Lvl Clouds Type-CM',  # Cloud Amt Type Height Lvl3
            'Val_Elem171': 'High Lvl Clouds Type-CH',  # Cloud Amt Type Height Lvl4

            'Val_Elem119': 'Vertical Significance 1',  # Cloud Opacity  Lvl1
            'Val_Elem116': 'Cloud Amt Lvl1-N1',  # Cloud Amt  Lvl 1
            'Val_Elem117': 'Cloud Type Lvl1-C1',  # Cloud Type  Low
            'Val_Elem118': 'Cloud Ht Lvl1-HsHs1',  # Cloud Height  Lvl 1
            'Val_Elem123': 'Vertical Significance 2',  # Cloud Opacity  lvl2
            'Val_Elem120': 'Cloud Amt Lvl2-N2',  # Cloud Amt  Lvl 2
            'Val_Elem121': 'Cloud Type Lv2-C2',  # Cloud Type  Lvl 2
            'Val_Elem122': 'Cloud Ht Lvl2-HsHs2',  # Cloud Height  Lvl 2
            'Val_Elem127': 'Vertical Significant 3',  # Cloud Opacity  Lvl3
            'Val_Elem124': 'Cloud Amt Lvl3-N3',  # Cloud Amt  Lvl 3
            'Val_Elem125': 'Cloud Type Lvl3-C3',  # Cloud Type  Lvl 3
            'Val_Elem126': 'Cloud Ht Lvl3-HsHs3',  # Cloud Height  Lvl 3
            'Val_Elem131': 'Vertical Significance 4',  # Cloud Opacity  Lvl4
            'Val_Elem128': 'Cloud Amt Lvl4-N4',  # Cloud Amt  Lvl 4
            'Val_Elem129': 'Cloud Type Lvl4-C4',  # Cloud Type  Lvl 4
            'Val_Elem130': 'Cloud Ht Lvl4-Hshs4',  # Cloud Height  Lvl 4

            'Val_Elem167': 'PresentWx',  # Present Weather
            'Val_Elem197': 'PastWx1',  # Visibility Max
            'Val_Elem193': 'PastWx2',  # Cloud  Medium Lvl  Type
            'Val_Elem002': 'Tmax',  # Temp  Daily Max
            'Val_Elem003': 'Tmin',  # Temp  Daily Min
            'Val_Elem099': 'Grass Min Temp',  # Wind Totalizer  06Z
            'Val_Elem018': 'Evaporation',  # Evap  Pan1 Daily
            'Val_Elem084': 'SSS-24Hr',  # Sunshine  Daily Tot
            'Val_Elem132': 'SSS-1Hr',  # Sunshine Hly Tot
            'Val_Elem005': 'Precip-24Hr',  # Precip  Daily
            'Val_Elem174': 'Precip-3Hr',  # Precip  Tot 3 Hours
            'Val_Elem112': 'Wind Direction-dd',  # Wind Direction
            'Val_Elem111': 'Wind Speed - fff',  # Wind Speed in Knots
            'Val_Elem046': 'Insolation - Rad',  # Insolation Daily

            'Flag106': '',
            'Flag107': '',
            'Flag400': '',
            'Flag814': '',
            'Flag399': '',
            'Flag301': '',
            'Flag185': '',
            'Flag101': '',
            'Flag102': '',
            'Flag103': '',
            'Flag105': '',
            'Flag192': '',
            'Flag110': '',
            'Flag114': '',
            'Flag112': '',
            'Flag111': '',
            'Flag167': '',
            'Flag197': '',
            'Flag193': '',
            'Flag115': '',
            'Flag168': '',
            'Flag169': '',
            'Flag170': '',
            'Flag171': '',
            'Flag119': '',
            'Flag116': '',
            'Flag117': '',
            'Flag118': '',
            'Flag123': '',
            'Flag120': '',
            'Flag121': '',
            'Flag122': '',
            'Flag127': '',
            'Flag124': '',
            'Flag125': '',
            'Flag126': '',
            'Flag131': '',
            'Flag128': '',
            'Flag129': '',
            'Flag130': '',
            'Flag002': '',
            'Flag003': '',
            'Flag099': '',
            'Flag018': '',
            'Flag084': '',
            'Flag132': '',
            'Flag005': '',
            'Flag174': '',
            'Flag046': '',
        }
        include = labels.keys()

    def columns(self):
        return [
            [ValueFlag(self['Val_Elem{}'.format(field_num)], self['Flag{}'.format(field_num)]) for field_num in column]
            for column in self.COLUMNS
        ]