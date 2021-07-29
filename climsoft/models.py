# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Temporary solution to include bind_key in each db_Table and db_Model declaration
def db_Table(*args, **kwargs):
    return db.Table(*args, **kwargs, info={'bind_key': 'climsoft4_prod'}
)
class db_Model(db.Model):
    __abstract__ = True
    __bind_key__ = 'climsoft4_prod'


t_abc = db_Table(
    'abc',
    db.Column('No', db.Integer, nullable=False, unique=True),
    db.Column('Element_abbreviation', db.Text, nullable=False),
    db.Column('Element_Name', db.Text, nullable=False),
    db.Column('Element_Details', db.Text, nullable=False),
    db.Column('Climsoft_Element', db.Text, nullable=False),
    db.Column('Bufr_Element', db.Text, nullable=False),
    db.Column('unit', db.Text, nullable=False),
    db.Column('lower_limit', db.Text, nullable=False),
    db.Column('upper_limit', db.Text, nullable=False),
    db.Column('obsv', db.Text, nullable=False)
)



class Acquisitiontype(db_Model):
    __tablename__ = 'acquisitiontype'

    code = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    description = db.Column(db.String(255))



t_aws1 = db_Table(
    'aws1',
    db.Column('No', db.Integer, nullable=False, unique=True),
    db.Column('Element_abbreviation', db.Text, nullable=False),
    db.Column('Element_Name', db.Text, nullable=False),
    db.Column('Element_Details', db.Text, nullable=False),
    db.Column('Climsoft_Element', db.Text, nullable=False),
    db.Column('Bufr_Element', db.Text, nullable=False),
    db.Column('unit', db.Text, nullable=False),
    db.Column('lower_limit', db.Text, nullable=False),
    db.Column('upper_limit', db.Text, nullable=False),
    db.Column('obsv', db.Text, nullable=False)
)



class AwsBasestation(db_Model):
    __tablename__ = 'aws_basestation'

    ftpId = db.Column(db.String(50), primary_key=True, unique=True)
    inputFolder = db.Column(db.String(20), nullable=False)
    ftpMode = db.Column(db.String(10))
    userName = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)



class AwsElement(db_Model):
    __tablename__ = 'aws_elements'

    aws_element = db.Column(db.String(50), primary_key=True, nullable=False)
    climsoft_element = db.Column(db.String(50), primary_key=True, nullable=False)
    element_description = db.Column(db.String(50), nullable=False)



class AwsMalawi1(db_Model):
    __tablename__ = 'aws_malawi1'

    Cols = db.Column(db.Integer, primary_key=True)
    Element_abbreviation = db.Column(db.String(50))
    Element_Name = db.Column(db.String(50), index=True)
    Element_Details = db.Column(db.String(50))
    Climsoft_Element = db.Column(db.String(6))
    Bufr_Element = db.Column(db.String(6))
    unit = db.Column(db.String(15))
    lower_limit = db.Column(db.String(50))
    upper_limit = db.Column(db.String(50))
    obsv = db.Column(db.String(50))



t_aws_malawi12 = db_Table(
    'aws_malawi12',
    db.Column('No', db.Integer, nullable=False, unique=True),
    db.Column('Element_abbreviation', db.Text, nullable=False),
    db.Column('Element_Name', db.Text, nullable=False),
    db.Column('Element_Details', db.Text, nullable=False),
    db.Column('Climsoft_Element', db.Text, nullable=False),
    db.Column('Bufr_Element', db.Text, nullable=False),
    db.Column('unit', db.Text, nullable=False),
    db.Column('lower_limit', db.Text, nullable=False),
    db.Column('upper_limit', db.Text, nullable=False),
    db.Column('obsv', db.Text, nullable=False)
)



class AwsMs(db_Model):
    __tablename__ = 'aws_mss'

    ftpId = db.Column(db.String(50), primary_key=True)
    inputFolder = db.Column(db.String(20), nullable=False)
    userName = db.Column(db.String(15), nullable=False)
    ftpMode = db.Column(db.String(10))
    password = db.Column(db.String(15))



class AwsProcessParameter(db_Model):
    __tablename__ = 'aws_process_parameters'

    RetrieveInterval = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    HourOffset = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    RetrievePeriod = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    RetrieveTimeout = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    DelinputFile = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    UTCDiff = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



t_aws_rwanda1 = db_Table(
    'aws_rwanda1',
    db.Column('Cols', db.Integer, server_default=db.FetchedValue()),
    db.Column('Element_abbreviation', db.String(50)),
    db.Column('Element_Name', db.String(50), index=True),
    db.Column('Element_Details', db.String(50)),
    db.Column('Climsoft_Element', db.String(6)),
    db.Column('Bufr_Element', db.String(6)),
    db.Column('unit', db.String(15)),
    db.Column('lower_limit', db.String(50)),
    db.Column('upper_limit', db.String(50)),
    db.Column('obsv', db.String(50))
)



class AwsRwanda4(db_Model):
    __tablename__ = 'aws_rwanda4'

    Cols = db.Column(db.Integer, primary_key=True)
    Element_Name = db.Column(db.String(20))
    Element_Abbreviation = db.Column(db.String(20))
    Element_Details = db.Column(db.String(25))
    Climsoft_Element = db.Column(db.String(6))
    Bufr_Element = db.Column(db.String(6))
    unit = db.Column(db.String(15))
    lower_limit = db.Column(db.String(10))
    upper_limit = db.Column(db.String(10))
    obsv = db.Column(db.String(25))



class AwsSasscal1(db_Model):
    __tablename__ = 'aws_sasscal1'

    Cols = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    Element_Abbreviation = db.Column(db.String(50))
    Element_Name = db.Column(db.String(50))
    Element_Details = db.Column(db.String(50))
    Climsoft_Element = db.Column(db.String(6))
    Bufr_Element = db.Column(db.String(6))
    unit = db.Column(db.String(15))
    lower_limit = db.Column(db.String(50))
    upper_limit = db.Column(db.String(50))
    obsv = db.Column(db.String(50))



class AwsSite(db_Model):
    __tablename__ = 'aws_sites'

    SiteID = db.Column(db.String(20), primary_key=True, unique=True)
    SiteName = db.Column(db.String(50))
    InputFile = db.Column(db.String(50))
    FilePrefix = db.Column(db.String(50))
    chkPrefix = db.Column(db.Integer, server_default=db.FetchedValue())
    DataStructure = db.Column(db.String(50))
    MissingDataFlag = db.Column(db.String(10))
    awsServerIP = db.Column(db.String(50))
    OperationalStatus = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    GTSEncode = db.Column(db.String(20))
    GTSHeader = db.Column(db.String(20))



class AwsStation(db_Model):
    __tablename__ = 'aws_stations'

    aws_id = db.Column(db.String(50), primary_key=True, nullable=False)
    national_id = db.Column(db.String(50), primary_key=True, nullable=False)
    station_name = db.Column(db.String(50))



class AwsStructure(db_Model):
    __tablename__ = 'aws_structures'

    strID = db.Column(db.Integer, nullable=False, unique=True)
    strName = db.Column(db.String(20), primary_key=True)
    data_delimiter = db.Column(db.String(10), nullable=False)
    hdrRows = db.Column(db.Integer, nullable=False)
    txtQualifier = db.Column(db.String(5))



class AwsTahmo(db_Model):
    __tablename__ = 'aws_tahmo'

    Cols = db.Column(db.Integer, primary_key=True)
    Element_abbreviation = db.Column(db.String(50))
    Element_Name = db.Column(db.String(50))
    Element_Details = db.Column(db.String(50))
    Climsoft_Element = db.Column(db.String(6))
    Bufr_Element = db.Column(db.String(6))
    unit = db.Column(db.String(15))
    lower_limit = db.Column(db.String(50))
    upper_limit = db.Column(db.String(50))
    obsv = db.Column(db.String(50))



t_aws_toa5_bw1 = db_Table(
    'aws_toa5_bw1',
    db.Column('Cols', db.Integer, server_default=db.FetchedValue()),
    db.Column('Element_Abbreviation', db.String(50), unique=True),
    db.Column('Element_Name', db.String(50)),
    db.Column('Element_Details', db.String(50)),
    db.Column('Climsoft_Element', db.String(6)),
    db.Column('Bufr_Element', db.String(6)),
    db.Column('unit', db.String(15)),
    db.Column('lower_limit', db.String(50)),
    db.Column('upper_limit', db.String(50)),
    db.Column('obsv', db.String(50))
)



class AwsToa5Mg2(db_Model):
    __tablename__ = 'aws_toa5_mg2'

    Cols = db.Column(db.BigInteger, primary_key=True)
    Element_Abbreviation = db.Column(db.String(50))
    Element_Name = db.Column(db.String(50))
    Element_Details = db.Column(db.String(50))
    Climsoft_Element = db.Column(db.String(6))
    Bufr_Element = db.Column(db.String(6))
    unit = db.Column(db.String(15))
    lower_limit = db.Column(db.String(50))
    upper_limit = db.Column(db.String(50))
    obsv = db.Column(db.String(50))



t_bufr_crex_data = db_Table(
    'bufr_crex_data',
    db.Column('nos', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('Crex_Unit', db.String(25)),
    db.Column('Crex_Scale', db.String(25), nullable=False),
    db.Column('Crex_DataWidth', db.String(25), nullable=False),
    db.Column('Bufr_Unit', db.String(255), nullable=False),
    db.Column('Bufr_Scale', db.String(25), nullable=False, server_default=db.FetchedValue()),
    db.Column('Bufr_RefValue', db.String(50), server_default=db.FetchedValue()),
    db.Column('Bufr_DataWidth_Bits', db.String(50), server_default=db.FetchedValue()),
    db.Column('selected', db.Integer),
    db.Column('Observation', db.String(255)),
    db.Column('Crex_Data', db.String(30)),
    db.Column('Bufr_Data', db.String(255), server_default=db.FetchedValue())
)



t_bufr_crex_master = db_Table(
    'bufr_crex_master',
    db.Column('Bufr_FXY', db.String(6), nullable=False),
    db.Column('Crex_Fxxyyy', db.String(255), nullable=False),
    db.Column('ElementName', db.String(255), nullable=False),
    db.Column('Bufr_Unit', db.String(255), nullable=False),
    db.Column('Bufr_Scale', db.String(25), nullable=False, server_default=db.FetchedValue()),
    db.Column('Bufr_RefValue', db.String(50), server_default=db.FetchedValue()),
    db.Column('Bufr_DataWidth_Bits', db.String(50), server_default=db.FetchedValue()),
    db.Column('Crex_Unit', db.String(25)),
    db.Column('Crex_Scale', db.String(25), nullable=False),
    db.Column('Crex_DataWidth', db.String(25), nullable=False),
    db.Column('Observation', db.String(255)),
    db.Column('Crex_Data', db.String(30)),
    db.Column('Bufr_Data', db.String(255), server_default=db.FetchedValue())
)



class BufrIndicator(db_Model):
    __tablename__ = 'bufr_indicators'

    Tmplate = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue())
    Msg_Header = db.Column(db.String(50), server_default=db.FetchedValue())
    BUFR_Edition = db.Column(db.String(10), server_default=db.FetchedValue())
    Originating_Centre = db.Column(db.String(10), server_default=db.FetchedValue())
    Originating_SubCentre = db.Column(db.String(10), server_default=db.FetchedValue())
    Update_Sequence = db.Column(db.String(10), server_default=db.FetchedValue())
    Optional_Section = db.Column(db.String(10), server_default=db.FetchedValue())
    Data_Category = db.Column(db.String(10), server_default=db.FetchedValue())
    Intenational_Data_SubCategory = db.Column(db.String(10), server_default=db.FetchedValue())
    Local_Data_SubCategory = db.Column(db.String(10), server_default=db.FetchedValue())
    Master_table = db.Column(db.String(10), server_default=db.FetchedValue())
    Local_Table = db.Column(db.String(10), server_default=db.FetchedValue())



t_ccitt = db_Table(
    'ccitt',
    db.Column('Characters', db.String(25)),
    db.Column('MostSignificant', db.Integer),
    db.Column('LeastSignificant', db.Integer)
)



class Climsoftuser(db_Model):
    __tablename__ = 'climsoftusers'

    userName = db.Column(db.String(50), primary_key=True)
    userRole = db.Column(db.String(50), nullable=False)



class CodeFlag(db_Model):
    __tablename__ = 'code_flag'

    FXY = db.Column(db.String(255), primary_key=True)
    Fxyyy = db.Column(db.String(50))
    Description = db.Column(db.String(255))
    Bufr_DataWidth_Bits = db.Column(db.Integer)
    Crex_DataWidth = db.Column(db.String(25))
    Bufr_Unit = db.Column(db.String(255))
    Bufr_Value = db.Column(db.String(50))
    Crex_Value = db.Column(db.String(10))



class DataForm(db_Model):
    __tablename__ = 'data_forms'

    id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    order_num = db.Column(db.BigInteger, server_default=db.FetchedValue())
    table_name = db.Column(db.String(255))
    form_name = db.Column(db.String(250), primary_key=True)
    description = db.Column(db.Text)
    selected = db.Column(db.Integer)
    val_start_position = db.Column(db.BigInteger, server_default=db.FetchedValue())
    val_end_position = db.Column(db.BigInteger, server_default=db.FetchedValue())
    elem_code_location = db.Column(db.String(255))
    sequencer = db.Column(db.String(50))
    entry_mode = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



t_faultresolution = db_Table(
    'faultresolution',
    db.Column('resolvedDatetime', db.String(50)),
    db.Column('resolvedBy', db.String(255)),
    db.Column('associatedWith', db.ForeignKey('instrumentfaultreport.reportId'), index=True),
    db.Column('remarks', db.String(255)),
    db.Index('solution', 'resolvedDatetime', 'associatedWith')
)



t_featuregeographicalposition = db_Table(
    'featuregeographicalposition',
    db.Column('belongsTo', db.ForeignKey('synopfeature.abbreviation'), nullable=False),
    db.Column('observedOn', db.String(50)),
    db.Column('latitude', db.Float(11, True)),
    db.Column('longitude', db.Float(11, True)),
    db.Index('FK_mysql_climsoft_db_v4_synopfeatureFeatureGeographicalPosition', 'belongsTo', 'observedOn')
)



class Flag(db_Model):
    __tablename__ = 'flags'

    characterSymbol = db.Column(db.String(255), primary_key=True, server_default=db.FetchedValue())
    numSymbol = db.Column(db.Integer)
    description = db.Column(db.String(255))



class Flagtable(db_Model):
    __tablename__ = 'flagtable'

    Bufr_Descriptor = db.Column(db.String(6), primary_key=True)
    Crex_Descriptor = db.Column(db.String(6))
    Details = db.Column(db.String(255))
    Widths = db.Column(db.Integer, server_default=db.FetchedValue())
    Missing = db.Column(db.Integer, server_default=db.FetchedValue())



class FormAgro1(db_Model):
    __tablename__ = 'form_agro1'

    stationId = db.Column(db.String(50), primary_key=True, nullable=False, server_default=db.FetchedValue())
    yyyy = db.Column(db.Integer, primary_key=True, nullable=False)
    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)
    Val_Elem101 = db.Column(db.String(6))
    Val_Elem102 = db.Column(db.String(6))
    Val_Elem103 = db.Column(db.String(6))
    Val_Elem105 = db.Column(db.String(6))
    Val_Elem002 = db.Column(db.String(6))
    Val_Elem003 = db.Column(db.String(6))
    Val_Elem099 = db.Column(db.String(6))
    Val_Elem072 = db.Column(db.String(6))
    Val_Elem073 = db.Column(db.String(6))
    Val_Elem074 = db.Column(db.String(6))
    Val_Elem554 = db.Column(db.String(6))
    Val_Elem075 = db.Column(db.String(6))
    Val_Elem076 = db.Column(db.String(6))
    Val_Elem561 = db.Column(db.String(6))
    Val_Elem562 = db.Column(db.String(6))
    Val_Elem563 = db.Column(db.String(6))
    Val_Elem513 = db.Column(db.String(6))
    Val_Elem005 = db.Column(db.String(6))
    Val_Elem504 = db.Column(db.String(6))
    Val_Elem532 = db.Column(db.String(6))
    Val_Elem137 = db.Column(db.String(6))
    Val_Elem018 = db.Column(db.String(6))
    Val_Elem518 = db.Column(db.String(6))
    Val_Elem511 = db.Column(db.String(6))
    Val_Elem512 = db.Column(db.String(6))
    Val_Elem503 = db.Column(db.String(6))
    Val_Elem515 = db.Column(db.String(6))
    Val_Elem564 = db.Column(db.String(6))
    Val_Elem565 = db.Column(db.String(6))
    Val_Elem566 = db.Column(db.String(6))
    Val_Elem531 = db.Column(db.String(6))
    Val_Elem530 = db.Column(db.String(6))
    Val_Elem541 = db.Column(db.String(6))
    Val_Elem542 = db.Column(db.String(6))
    Flag101 = db.Column(db.String(1))
    Flag102 = db.Column(db.String(1))
    Flag103 = db.Column(db.String(1))
    Flag105 = db.Column(db.String(1))
    Flag002 = db.Column(db.String(1))
    Flag003 = db.Column(db.String(1))
    Flag099 = db.Column(db.String(1))
    Flag072 = db.Column(db.String(1))
    Flag073 = db.Column(db.String(1))
    Flag074 = db.Column(db.String(1))
    Flag554 = db.Column(db.String(1))
    Flag075 = db.Column(db.String(1))
    Flag076 = db.Column(db.String(1))
    Flag561 = db.Column(db.String(1))
    Flag562 = db.Column(db.String(1))
    Flag563 = db.Column(db.String(1))
    Flag513 = db.Column(db.String(1))
    Flag005 = db.Column(db.String(1))
    Flag504 = db.Column(db.String(1))
    Flag532 = db.Column(db.String(1))
    Flag137 = db.Column(db.String(1))
    Flag018 = db.Column(db.String(1))
    Flag518 = db.Column(db.String(1))
    Flag511 = db.Column(db.String(1))
    Flag512 = db.Column(db.String(1))
    Flag503 = db.Column(db.String(1))
    Flag515 = db.Column(db.String(1))
    Flag564 = db.Column(db.String(1))
    Flag565 = db.Column(db.String(1))
    Flag566 = db.Column(db.String(1))
    Flag531 = db.Column(db.String(1))
    Flag530 = db.Column(db.String(1))
    Flag541 = db.Column(db.String(1))
    Flag542 = db.Column(db.String(1))
    signature = db.Column(db.String(45))
    entryDatetime = db.Column(db.DateTime)



class FormDaily2(db_Model):
    __tablename__ = 'form_daily2'

    stationId = db.Column(db.String(50), primary_key=True, nullable=False)
    elementId = db.Column(db.Integer, primary_key=True, nullable=False)
    yyyy = db.Column(db.Integer, primary_key=True, nullable=False)
    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    hh = db.Column(db.Integer, primary_key=True, nullable=False)
    day01 = db.Column(db.String(45))
    day02 = db.Column(db.String(45))
    day03 = db.Column(db.String(45))
    day04 = db.Column(db.String(45))
    day05 = db.Column(db.String(45))
    day06 = db.Column(db.String(45))
    day07 = db.Column(db.String(45))
    day08 = db.Column(db.String(45))
    day09 = db.Column(db.String(45))
    day10 = db.Column(db.String(45))
    day11 = db.Column(db.String(45))
    day12 = db.Column(db.String(45))
    day13 = db.Column(db.String(45))
    day14 = db.Column(db.String(45))
    day15 = db.Column(db.String(45))
    day16 = db.Column(db.String(45))
    day17 = db.Column(db.String(45))
    day18 = db.Column(db.String(45))
    day19 = db.Column(db.String(45))
    day20 = db.Column(db.String(45))
    day21 = db.Column(db.String(45))
    day22 = db.Column(db.String(45))
    day23 = db.Column(db.String(45))
    day24 = db.Column(db.String(45))
    day25 = db.Column(db.String(45))
    day26 = db.Column(db.String(45))
    day27 = db.Column(db.String(45))
    day28 = db.Column(db.String(45))
    day29 = db.Column(db.String(45))
    day30 = db.Column(db.String(45))
    day31 = db.Column(db.String(45))
    flag01 = db.Column(db.String(1))
    flag02 = db.Column(db.String(1))
    flag03 = db.Column(db.String(1))
    flag04 = db.Column(db.String(1))
    flag05 = db.Column(db.String(1))
    flag06 = db.Column(db.String(1))
    flag07 = db.Column(db.String(1))
    flag08 = db.Column(db.String(1))
    flag09 = db.Column(db.String(1))
    flag10 = db.Column(db.String(1))
    flag11 = db.Column(db.String(1))
    flag12 = db.Column(db.String(1))
    flag13 = db.Column(db.String(1))
    flag14 = db.Column(db.String(1))
    flag15 = db.Column(db.String(1))
    flag16 = db.Column(db.String(1))
    flag17 = db.Column(db.String(1))
    flag18 = db.Column(db.String(1))
    flag19 = db.Column(db.String(1))
    flag20 = db.Column(db.String(1))
    flag21 = db.Column(db.String(1))
    flag22 = db.Column(db.String(1))
    flag23 = db.Column(db.String(1))
    flag24 = db.Column(db.String(1))
    flag25 = db.Column(db.String(1))
    flag26 = db.Column(db.String(1))
    flag27 = db.Column(db.String(1))
    flag28 = db.Column(db.String(1))
    flag29 = db.Column(db.String(1))
    flag30 = db.Column(db.String(1))
    flag31 = db.Column(db.String(1))
    period01 = db.Column(db.String(45))
    period02 = db.Column(db.String(45))
    period03 = db.Column(db.String(45))
    period04 = db.Column(db.String(45))
    period05 = db.Column(db.String(45))
    period06 = db.Column(db.String(45))
    period07 = db.Column(db.String(45))
    period08 = db.Column(db.String(45))
    period09 = db.Column(db.String(45))
    period10 = db.Column(db.String(45))
    period11 = db.Column(db.String(45))
    period12 = db.Column(db.String(45))
    period13 = db.Column(db.String(45))
    period14 = db.Column(db.String(45))
    period15 = db.Column(db.String(45))
    period16 = db.Column(db.String(45))
    period17 = db.Column(db.String(45))
    period18 = db.Column(db.String(45))
    period19 = db.Column(db.String(45))
    period20 = db.Column(db.String(45))
    period21 = db.Column(db.String(45))
    period22 = db.Column(db.String(45))
    period23 = db.Column(db.String(45))
    period24 = db.Column(db.String(45))
    period25 = db.Column(db.String(45))
    period26 = db.Column(db.String(45))
    period27 = db.Column(db.String(45))
    period28 = db.Column(db.String(45))
    period29 = db.Column(db.String(45))
    period30 = db.Column(db.String(45))
    period31 = db.Column(db.String(45))
    total = db.Column(db.String(45))
    signature = db.Column(db.String(45))
    entryDatetime = db.Column(db.DateTime)
    temperatureUnits = db.Column(db.String(45))
    precipUnits = db.Column(db.String(45))
    cloudHeightUnits = db.Column(db.String(45))
    visUnits = db.Column(db.String(45))



class FormHourly(db_Model):
    __tablename__ = 'form_hourly'

    stationId = db.Column(db.String(50), primary_key=True, nullable=False)
    elementId = db.Column(db.Integer, primary_key=True, nullable=False)
    yyyy = db.Column(db.Integer, primary_key=True, nullable=False)
    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)
    hh_00 = db.Column(db.String(50))
    hh_01 = db.Column(db.String(50))
    hh_02 = db.Column(db.String(50))
    hh_03 = db.Column(db.String(50))
    hh_04 = db.Column(db.String(50))
    hh_05 = db.Column(db.String(50))
    hh_06 = db.Column(db.String(50))
    hh_07 = db.Column(db.String(50))
    hh_08 = db.Column(db.String(50))
    hh_09 = db.Column(db.String(50))
    hh_10 = db.Column(db.String(50))
    hh_11 = db.Column(db.String(50))
    hh_12 = db.Column(db.String(50))
    hh_13 = db.Column(db.String(50))
    hh_14 = db.Column(db.String(50))
    hh_15 = db.Column(db.String(50))
    hh_16 = db.Column(db.String(50))
    hh_17 = db.Column(db.String(50))
    hh_18 = db.Column(db.String(50))
    hh_19 = db.Column(db.String(50))
    hh_20 = db.Column(db.String(50))
    hh_21 = db.Column(db.String(50))
    hh_22 = db.Column(db.String(50))
    hh_23 = db.Column(db.String(50))
    flag00 = db.Column(db.String(50))
    flag01 = db.Column(db.String(50))
    flag02 = db.Column(db.String(50))
    flag03 = db.Column(db.String(50))
    flag04 = db.Column(db.String(50))
    flag05 = db.Column(db.String(50))
    flag06 = db.Column(db.String(50))
    flag07 = db.Column(db.String(50))
    flag08 = db.Column(db.String(50))
    flag09 = db.Column(db.String(50))
    flag10 = db.Column(db.String(50))
    flag11 = db.Column(db.String(50))
    flag12 = db.Column(db.String(50))
    flag13 = db.Column(db.String(50))
    flag14 = db.Column(db.String(50))
    flag15 = db.Column(db.String(50))
    flag16 = db.Column(db.String(50))
    flag17 = db.Column(db.String(50))
    flag18 = db.Column(db.String(50))
    flag19 = db.Column(db.String(50))
    flag20 = db.Column(db.String(50))
    flag21 = db.Column(db.String(50))
    flag22 = db.Column(db.String(50))
    flag23 = db.Column(db.String(50))
    total = db.Column(db.String(50))
    signature = db.Column(db.String(50))
    entryDatetime = db.Column(db.DateTime)



class FormHourlyTimeSelection(db_Model):
    __tablename__ = 'form_hourly_time_selection'

    hh = db.Column(db.Integer, primary_key=True)
    hh_selection = db.Column(db.Integer)



class FormHourlywind(db_Model):
    __tablename__ = 'form_hourlywind'

    stationId = db.Column(db.String(255), primary_key=True, nullable=False)
    yyyy = db.Column(db.Integer, primary_key=True, nullable=False)
    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)
    elem_112_00 = db.Column(db.String(255))
    elem_112_01 = db.Column(db.String(255))
    elem_112_02 = db.Column(db.String(255))
    elem_112_03 = db.Column(db.String(255))
    elem_112_04 = db.Column(db.String(255))
    elem_112_05 = db.Column(db.String(255))
    elem_112_06 = db.Column(db.String(255))
    elem_112_07 = db.Column(db.String(255))
    elem_112_08 = db.Column(db.String(255))
    elem_112_09 = db.Column(db.String(255))
    elem_112_10 = db.Column(db.String(255))
    elem_112_11 = db.Column(db.String(255))
    elem_112_12 = db.Column(db.String(255))
    elem_112_13 = db.Column(db.String(255))
    elem_112_14 = db.Column(db.String(255))
    elem_112_15 = db.Column(db.String(255))
    elem_112_16 = db.Column(db.String(255))
    elem_112_17 = db.Column(db.String(255))
    elem_112_18 = db.Column(db.String(255))
    elem_112_19 = db.Column(db.String(255))
    elem_112_20 = db.Column(db.String(255))
    elem_112_21 = db.Column(db.String(255))
    elem_112_22 = db.Column(db.String(255))
    elem_112_23 = db.Column(db.String(255))
    ddflag00 = db.Column(db.String(255))
    ddflag01 = db.Column(db.String(255))
    ddflag02 = db.Column(db.String(255))
    ddflag03 = db.Column(db.String(255))
    ddflag04 = db.Column(db.String(255))
    ddflag05 = db.Column(db.String(255))
    ddflag06 = db.Column(db.String(255))
    ddflag07 = db.Column(db.String(255))
    ddflag08 = db.Column(db.String(255))
    ddflag09 = db.Column(db.String(255))
    ddflag10 = db.Column(db.String(255))
    ddflag11 = db.Column(db.String(255))
    ddflag12 = db.Column(db.String(255))
    ddflag13 = db.Column(db.String(255))
    ddflag14 = db.Column(db.String(255))
    ddflag15 = db.Column(db.String(255))
    ddflag16 = db.Column(db.String(255))
    ddflag17 = db.Column(db.String(255))
    ddflag18 = db.Column(db.String(255))
    ddflag19 = db.Column(db.String(255))
    ddflag20 = db.Column(db.String(255))
    ddflag21 = db.Column(db.String(255))
    ddflag22 = db.Column(db.String(255))
    ddflag23 = db.Column(db.String(255))
    elem_111_00 = db.Column(db.String(255))
    elem_111_01 = db.Column(db.String(255))
    elem_111_02 = db.Column(db.String(255))
    elem_111_03 = db.Column(db.String(255))
    elem_111_04 = db.Column(db.String(255))
    elem_111_05 = db.Column(db.String(255))
    elem_111_06 = db.Column(db.String(255))
    elem_111_07 = db.Column(db.String(255))
    elem_111_08 = db.Column(db.String(255))
    elem_111_09 = db.Column(db.String(255))
    elem_111_10 = db.Column(db.String(255))
    elem_111_11 = db.Column(db.String(255))
    elem_111_12 = db.Column(db.String(255))
    elem_111_13 = db.Column(db.String(255))
    elem_111_14 = db.Column(db.String(255))
    elem_111_15 = db.Column(db.String(255))
    elem_111_16 = db.Column(db.String(255))
    elem_111_17 = db.Column(db.String(255))
    elem_111_18 = db.Column(db.String(255))
    elem_111_19 = db.Column(db.String(255))
    elem_111_20 = db.Column(db.String(255))
    elem_111_21 = db.Column(db.String(255))
    elem_111_22 = db.Column(db.String(255))
    elem_111_23 = db.Column(db.String(255))
    total = db.Column(db.String(50))
    signature = db.Column(db.String(50))
    entryDatetime = db.Column(db.DateTime)



class FormMonthly(db_Model):
    __tablename__ = 'form_monthly'

    stationId = db.Column(db.String(255), primary_key=True, nullable=False)
    elementId = db.Column(db.Integer, primary_key=True, nullable=False)
    yyyy = db.Column(db.Integer, primary_key=True, nullable=False)
    mm_01 = db.Column(db.String(255))
    mm_02 = db.Column(db.String(255))
    mm_03 = db.Column(db.String(255))
    mm_04 = db.Column(db.String(255), nullable=False)
    mm_05 = db.Column(db.String(255))
    mm_06 = db.Column(db.String(255))
    mm_07 = db.Column(db.String(255))
    mm_08 = db.Column(db.String(255))
    mm_09 = db.Column(db.String(255))
    mm_10 = db.Column(db.String(255))
    mm_11 = db.Column(db.String(255))
    mm_12 = db.Column(db.String(255))
    flag01 = db.Column(db.String(255))
    flag02 = db.Column(db.String(255))
    flag03 = db.Column(db.String(255))
    flag04 = db.Column(db.String(255))
    flag05 = db.Column(db.String(255))
    flag06 = db.Column(db.String(255))
    flag07 = db.Column(db.String(255))
    flag08 = db.Column(db.String(255))
    flag09 = db.Column(db.String(255))
    flag10 = db.Column(db.String(255))
    flag11 = db.Column(db.String(255))
    flag12 = db.Column(db.String(255))
    period01 = db.Column(db.String(255))
    period02 = db.Column(db.String(255))
    period03 = db.Column(db.String(255))
    period04 = db.Column(db.String(255))
    period05 = db.Column(db.String(255))
    period06 = db.Column(db.String(255))
    period07 = db.Column(db.String(255))
    period08 = db.Column(db.String(255))
    period09 = db.Column(db.String(255))
    period10 = db.Column(db.String(255))
    period11 = db.Column(db.String(255))
    period12 = db.Column(db.String(255))
    signature = db.Column(db.String(50))
    entryDatetime = db.Column(db.DateTime)



class FormSynoptic2Tdcf(db_Model):
    __tablename__ = 'form_synoptic2_tdcf'
    __table_args__ = (
        db.Index('Identification', 'stationId', 'yyyy', 'mm', 'dd', 'hh'),
    )

    stationId = db.Column(db.String(10), primary_key=True, nullable=False)
    yyyy = db.Column(db.BigInteger, primary_key=True, nullable=False)
    mm = db.Column(db.BigInteger, primary_key=True, nullable=False)
    dd = db.Column(db.BigInteger, primary_key=True, nullable=False)
    hh = db.Column(db.String(5), primary_key=True, nullable=False)
    _106 = db.Column('106', db.String(6))
    _107 = db.Column('107', db.String(6))
    _399 = db.Column('399', db.String(5))
    _301 = db.Column('301', db.String(8))
    _185 = db.Column('185', db.String(6))
    _101 = db.Column('101', db.String(5))
    _103 = db.Column('103', db.String(5))
    _105 = db.Column('105', db.String(50))
    _110 = db.Column('110', db.String(5))
    _114 = db.Column('114', db.String(5))
    _115 = db.Column('115', db.String(5))
    _168 = db.Column('168', db.String(5))
    _192 = db.Column('192', db.String(5))
    _169 = db.Column('169', db.String(5))
    _170 = db.Column('170', db.String(5))
    _171 = db.Column('171', db.String(5))
    _119 = db.Column('119', db.String(5))
    _116 = db.Column('116', db.String(5))
    _117 = db.Column('117', db.String(5))
    _118 = db.Column('118', db.String(5))
    _123 = db.Column('123', db.String(5))
    _120 = db.Column('120', db.String(5))
    _121 = db.Column('121', db.String(5))
    _122 = db.Column('122', db.String(5))
    _127 = db.Column('127', db.String(5))
    _124 = db.Column('124', db.String(5))
    _125 = db.Column('125', db.String(5))
    _126 = db.Column('126', db.String(5))
    _131 = db.Column('131', db.String(5))
    _128 = db.Column('128', db.String(5))
    _129 = db.Column('129', db.String(5))
    _130 = db.Column('130', db.String(5))
    _167 = db.Column('167', db.String(5))
    _197 = db.Column('197', db.String(50))
    _193 = db.Column('193', db.String(5))
    _18 = db.Column('18', db.String(6))
    _532 = db.Column('532', db.String(6))
    _132 = db.Column('132', db.String(6))
    _5 = db.Column('5', db.String(6))
    _174 = db.Column('174', db.String(50))
    _3 = db.Column('3', db.String(5))
    _2 = db.Column('2', db.String(5))
    _112 = db.Column('112', db.String(5))
    _111 = db.Column('111', db.String(5))
    _85 = db.Column('85', db.String(50))
    flag1 = db.Column(db.String(1))
    flag2 = db.Column(db.String(1))
    flag3 = db.Column(db.String(1))
    flag4 = db.Column(db.String(1))
    flag5 = db.Column(db.String(1))
    flag6 = db.Column(db.String(1))
    flag7 = db.Column(db.String(1))
    flag8 = db.Column(db.String(1))
    flag9 = db.Column(db.String(1))
    flag10 = db.Column(db.String(1))
    flag11 = db.Column(db.String(1))
    flag12 = db.Column(db.String(1))
    flag13 = db.Column(db.String(1))
    flag14 = db.Column(db.String(1))
    flag15 = db.Column(db.String(1))
    flag16 = db.Column(db.String(1))
    flag17 = db.Column(db.String(1))
    flag18 = db.Column(db.String(1))
    flag19 = db.Column(db.String(1))
    flag20 = db.Column(db.String(1))
    flag21 = db.Column(db.String(1))
    flag22 = db.Column(db.String(1))
    flag23 = db.Column(db.String(1))
    flag24 = db.Column(db.String(1))
    flag25 = db.Column(db.String(1))
    flag26 = db.Column(db.String(1))
    flag27 = db.Column(db.String(1))
    flag28 = db.Column(db.String(1))
    flag29 = db.Column(db.String(1))
    flag30 = db.Column(db.String(1))
    flag31 = db.Column(db.String(1))
    flag32 = db.Column(db.String(1))
    flag33 = db.Column(db.String(1))
    flag34 = db.Column(db.String(1))
    flag35 = db.Column(db.String(1))
    flag36 = db.Column(db.String(1))
    flag37 = db.Column(db.String(1))
    flag38 = db.Column(db.String(1))
    flag39 = db.Column(db.String(1))
    flag40 = db.Column(db.String(1))
    flag41 = db.Column(db.String(1))
    flag42 = db.Column(db.String(1))
    flag43 = db.Column(db.String(1))
    flag44 = db.Column(db.String(1))
    flag45 = db.Column(db.String(1))
    signature = db.Column(db.String(50))
    entryDatetime = db.Column(db.DateTime)



class FormSynoptic2Ra1(db_Model):
    __tablename__ = 'form_synoptic_2_ra1'

    stationId = db.Column(db.String(50), primary_key=True, nullable=False, server_default=db.FetchedValue())
    yyyy = db.Column(db.Integer, primary_key=True, nullable=False)
    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)
    hh = db.Column(db.Integer, primary_key=True, nullable=False)
    Val_Elem106 = db.Column(db.String(6))
    Val_Elem107 = db.Column(db.String(6))
    Val_Elem400 = db.Column(db.String(6))
    Val_Elem814 = db.Column(db.String(6))
    Val_Elem399 = db.Column(db.String(6))
    Val_Elem301 = db.Column(db.String(6))
    Val_Elem185 = db.Column(db.String(6))
    Val_Elem101 = db.Column(db.String(6))
    Val_Elem102 = db.Column(db.String(6))
    Val_Elem103 = db.Column(db.String(6))
    Val_Elem105 = db.Column(db.String(6))
    Val_Elem192 = db.Column(db.String(6))
    Val_Elem110 = db.Column(db.String(6))
    Val_Elem114 = db.Column(db.String(6))
    Val_Elem112 = db.Column(db.String(6))
    Val_Elem111 = db.Column(db.String(6))
    Val_Elem167 = db.Column(db.String(6))
    Val_Elem197 = db.Column(db.String(6))
    Val_Elem193 = db.Column(db.String(6))
    Val_Elem115 = db.Column(db.String(6))
    Val_Elem168 = db.Column(db.String(6))
    Val_Elem169 = db.Column(db.String(6))
    Val_Elem170 = db.Column(db.String(6))
    Val_Elem171 = db.Column(db.String(6))
    Val_Elem119 = db.Column(db.String(6))
    Val_Elem116 = db.Column(db.String(6))
    Val_Elem117 = db.Column(db.String(6))
    Val_Elem118 = db.Column(db.String(6))
    Val_Elem123 = db.Column(db.String(6))
    Val_Elem120 = db.Column(db.String(6))
    Val_Elem121 = db.Column(db.String(6))
    Val_Elem122 = db.Column(db.String(6))
    Val_Elem127 = db.Column(db.String(6))
    Val_Elem124 = db.Column(db.String(6))
    Val_Elem125 = db.Column(db.String(6))
    Val_Elem126 = db.Column(db.String(6))
    Val_Elem131 = db.Column(db.String(6))
    Val_Elem128 = db.Column(db.String(6))
    Val_Elem129 = db.Column(db.String(6))
    Val_Elem130 = db.Column(db.String(6))
    Val_Elem002 = db.Column(db.String(6))
    Val_Elem003 = db.Column(db.String(6))
    Val_Elem099 = db.Column(db.String(6))
    Val_Elem018 = db.Column(db.String(6))
    Val_Elem084 = db.Column(db.String(6))
    Val_Elem132 = db.Column(db.String(6))
    Val_Elem005 = db.Column(db.String(6))
    Val_Elem174 = db.Column(db.String(6))
    Val_Elem046 = db.Column(db.String(6))
    Flag106 = db.Column(db.String(1))
    Flag107 = db.Column(db.String(1))
    Flag400 = db.Column(db.String(1))
    Flag814 = db.Column(db.String(1))
    Flag399 = db.Column(db.String(1))
    Flag301 = db.Column(db.String(1))
    Flag185 = db.Column(db.String(1))
    Flag101 = db.Column(db.String(1))
    Flag102 = db.Column(db.String(1))
    Flag103 = db.Column(db.String(1))
    Flag105 = db.Column(db.String(1))
    Flag192 = db.Column(db.String(1))
    Flag110 = db.Column(db.String(1))
    Flag114 = db.Column(db.String(1))
    Flag112 = db.Column(db.String(1))
    Flag111 = db.Column(db.String(1))
    Flag167 = db.Column(db.String(1))
    Flag197 = db.Column(db.String(1))
    Flag193 = db.Column(db.String(1))
    Flag115 = db.Column(db.String(1))
    Flag168 = db.Column(db.String(1))
    Flag169 = db.Column(db.String(1))
    Flag170 = db.Column(db.String(1))
    Flag171 = db.Column(db.String(1))
    Flag119 = db.Column(db.String(1))
    Flag116 = db.Column(db.String(1))
    Flag117 = db.Column(db.String(1))
    Flag118 = db.Column(db.String(1))
    Flag123 = db.Column(db.String(1))
    Flag120 = db.Column(db.String(1))
    Flag121 = db.Column(db.String(1))
    Flag122 = db.Column(db.String(1))
    Flag127 = db.Column(db.String(1))
    Flag124 = db.Column(db.String(1))
    Flag125 = db.Column(db.String(1))
    Flag126 = db.Column(db.String(1))
    Flag131 = db.Column(db.String(1))
    Flag128 = db.Column(db.String(1))
    Flag129 = db.Column(db.String(1))
    Flag130 = db.Column(db.String(1))
    Flag002 = db.Column(db.String(1))
    Flag003 = db.Column(db.String(1))
    Flag099 = db.Column(db.String(1))
    Flag018 = db.Column(db.String(1))
    Flag084 = db.Column(db.String(1))
    Flag132 = db.Column(db.String(1))
    Flag005 = db.Column(db.String(1))
    Flag174 = db.Column(db.String(1))
    Flag046 = db.Column(db.String(1))
    signature = db.Column(db.String(45))
    entryDatetime = db.Column(db.DateTime)



class Instrument(db_Model):
    __tablename__ = 'instrument'

    instrumentName = db.Column(db.String(255))
    instrumentId = db.Column(db.String(255), primary_key=True, index=True)
    serialNumber = db.Column(db.String(255))
    abbreviation = db.Column(db.String(255))
    model = db.Column(db.String(255))
    manufacturer = db.Column(db.String(255))
    instrumentUncertainty = db.Column(db.Float(11))
    installationDatetime = db.Column(db.String(50))
    deinstallationDatetime = db.Column(db.String(50))
    height = db.Column(db.String(255))
    instrumentPicture = db.Column(db.String(255))
    installedAt = db.Column(db.ForeignKey('station.stationId'), index=True)

    station = db.relationship('Station', primaryjoin='Instrument.installedAt == Station.stationId', backref='instruments')



class Instrumentfaultreport(db_Model):
    __tablename__ = 'instrumentfaultreport'
    __table_args__ = (
        db.Index('instrument_report', 'refersTo', 'reportDatetime', 'reportedFrom'),
    )

    refersTo = db.Column(db.ForeignKey('instrument.instrumentId'))
    reportId = db.Column(db.BigInteger, primary_key=True, index=True)
    reportDatetime = db.Column(db.String(50))
    faultDescription = db.Column(db.String(255))
    reportedBy = db.Column(db.String(255))
    receivedDatetime = db.Column(db.String(50))
    receivedBy = db.Column(db.String(255))
    reportedFrom = db.Column(db.ForeignKey('station.stationId'), index=True)

    instrument = db.relationship('Instrument', primaryjoin='Instrumentfaultreport.refersTo == Instrument.instrumentId', backref='instrumentfaultreports')
    station = db.relationship('Station', primaryjoin='Instrumentfaultreport.reportedFrom == Station.stationId', backref='instrumentfaultreports')



t_instrumentinspection = db_Table(
    'instrumentinspection',
    db.Column('performedOn', db.ForeignKey('instrument.instrumentId')),
    db.Column('inspectionDatetime', db.String(50)),
    db.Column('performedBy', db.String(255)),
    db.Column('status', db.String(255)),
    db.Column('remarks', db.String(255)),
    db.Column('performedAt', db.ForeignKey('station.stationId'), index=True),
    db.Index('inspection', 'performedOn', 'inspectionDatetime')
)



class LanguageTranslation(db_Model):
    __tablename__ = 'language_translation'

    tagID = db.Column(db.String(50), primary_key=True)
    en = db.Column(db.String(100))
    fr = db.Column(db.String(100))
    de = db.Column(db.String(100))
    pt = db.Column(db.String(100))



class MissingStat(db_Model):
    __tablename__ = 'missing_stats'

    STN_ID = db.Column(db.String(255), primary_key=True, nullable=False)
    ELEM = db.Column(db.BigInteger, primary_key=True, nullable=False)
    MISSING = db.Column(db.BigInteger)
    Closing_Date = db.Column(db.Date, primary_key=True, nullable=False)
    Opening_Date = db.Column(db.Date, primary_key=True, nullable=False)



class Obselement(db_Model):
    __tablename__ = 'obselement'

    elementId = db.Column(db.BigInteger, primary_key=True, index=True, server_default=db.FetchedValue())
    abbreviation = db.Column(db.String(255))
    elementName = db.Column(db.String(255))
    description = db.Column(db.String(255))
    elementScale = db.Column(db.Numeric(8, 2))
    upperLimit = db.Column(db.String(255))
    lowerLimit = db.Column(db.String(255))
    units = db.Column(db.String(255))
    elementtype = db.Column(db.String(50))
    qcTotalRequired = db.Column(db.Integer, server_default=db.FetchedValue())
    selected = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



t_observationfinal = db_Table(
    'observationfinal',
    db.Column('recordedFrom', db.ForeignKey('station.stationId'), nullable=False, index=True),
    db.Column('describedBy', db.ForeignKey('obselement.elementId'), index=True),
    db.Column('obsDatetime', db.DateTime),
    db.Column('obsLevel', db.String(255), server_default=db.FetchedValue()),
    db.Column('obsValue', db.Numeric(8, 2)),
    db.Column('flag', db.String(255), server_default=db.FetchedValue()),
    db.Column('period', db.Integer),
    db.Column('qcStatus', db.Integer, server_default=db.FetchedValue()),
    db.Column('qcTypeLog', db.Text),
    db.Column('acquisitionType', db.Integer, server_default=db.FetchedValue()),
    db.Column('dataForm', db.String(255)),
    db.Column('capturedBy', db.String(255)),
    db.Column('mark', db.Integer),
    db.Column('temperatureUnits', db.String(255)),
    db.Column('precipitationUnits', db.String(255)),
    db.Column('cloudHeightUnits', db.String(255)),
    db.Column('visUnits', db.String(255)),
    db.Column('dataSourceTimeZone', db.Integer, server_default=db.FetchedValue()),
    db.Index('obsFinalIdentification', 'recordedFrom', 'describedBy', 'obsDatetime')
)



t_observationinitial = db_Table(
    'observationinitial',
    db.Column('recordedFrom', db.ForeignKey('station.stationId'), nullable=False, index=True),
    db.Column('describedBy', db.ForeignKey('obselement.elementId'), index=True),
    db.Column('obsDatetime', db.DateTime),
    db.Column('obsLevel', db.String(255)),
    db.Column('obsValue', db.String(255)),
    db.Column('flag', db.String(255)),
    db.Column('period', db.Integer),
    db.Column('qcStatus', db.Integer, server_default=db.FetchedValue()),
    db.Column('qcTypeLog', db.Text),
    db.Column('acquisitionType', db.Integer, server_default=db.FetchedValue()),
    db.Column('dataForm', db.String(255)),
    db.Column('capturedBy', db.String(255)),
    db.Column('mark', db.Integer),
    db.Column('temperatureUnits', db.String(255)),
    db.Column('precipitationUnits', db.String(255)),
    db.Column('cloudHeightUnits', db.String(255)),
    db.Column('visUnits', db.String(255)),
    db.Column('dataSourceTimeZone', db.Integer, server_default=db.FetchedValue()),
    db.Index('obsInitialIdentification', 'recordedFrom', 'describedBy', 'obsDatetime', 'qcStatus', 'acquisitionType')
)



t_observationschedule = db_Table(
    'observationschedule',
    db.Column('classifiedInto', db.ForeignKey('obsscheduleclass.scheduleClass')),
    db.Column('startTime', db.String(50)),
    db.Column('endTime', db.String(50)),
    db.Column('interval', db.String(255)),
    db.Column('additionalObsTime', db.String(255)),
    db.Index('scheduleIdentification', 'classifiedInto', 'startTime', 'endTime')
)



class Obsscheduleclas(db_Model):
    __tablename__ = 'obsscheduleclass'

    scheduleClass = db.Column(db.String(255), primary_key=True, index=True, server_default=db.FetchedValue())
    description = db.Column(db.String(255))
    refersTo = db.Column(db.ForeignKey('station.stationId'), index=True)

    station = db.relationship('Station', primaryjoin='Obsscheduleclas.refersTo == Station.stationId', backref='obsscheduleclass')



t_paperarchive = db_Table(
    'paperarchive',
    db.Column('belongsTo', db.ForeignKey('station.stationId')),
    db.Column('formDatetime', db.DateTime),
    db.Column('image', db.String(255)),
    db.Column('classifiedInto', db.ForeignKey('paperarchivedefinition.formId'), index=True),
    db.Index('paper_archive_identification', 'belongsTo', 'formDatetime', 'classifiedInto')
)



class Paperarchivedefinition(db_Model):
    __tablename__ = 'paperarchivedefinition'

    formId = db.Column(db.String(50), primary_key=True, index=True)
    description = db.Column(db.String(255))



t_physicalfeature = db_Table(
    'physicalfeature',
    db.Column('associatedWith', db.ForeignKey('station.stationId'), nullable=False, index=True),
    db.Column('beginDate', db.String(50)),
    db.Column('endDate', db.String(50)),
    db.Column('image', db.String(255)),
    db.Column('description', db.String(255)),
    db.Column('classifiedInto', db.ForeignKey('physicalfeatureclass.featureClass'), index=True),
    db.Index('featureIdentification', 'associatedWith', 'beginDate', 'classifiedInto', 'description')
)



class Physicalfeatureclas(db_Model):
    __tablename__ = 'physicalfeatureclass'

    featureClass = db.Column(db.String(255), primary_key=True, index=True)
    description = db.Column(db.String(255))
    refersTo = db.Column(db.ForeignKey('station.stationId'), index=True)

    station = db.relationship('Station', primaryjoin='Physicalfeatureclas.refersTo == Station.stationId', backref='physicalfeatureclass')



class QcInterelement1(db_Model):
    __tablename__ = 'qc_interelement_1'

    stationId_1 = db.Column(db.String(50), primary_key=True, nullable=False)
    elementId_1 = db.Column(db.Integer, primary_key=True, nullable=False)
    obsDatetime_1 = db.Column(db.DateTime, primary_key=True, nullable=False)
    obsValue_1 = db.Column(db.Integer)
    qcStatus_1 = db.Column(db.Integer)
    acquisitionType_1 = db.Column(db.Integer)
    obsLevel_1 = db.Column(db.String(50))
    capturedBy_1 = db.Column(db.String(50))
    dataForm_1 = db.Column(db.String(50))



class QcInterelement2(db_Model):
    __tablename__ = 'qc_interelement_2'

    stationId_2 = db.Column(db.String(50), primary_key=True, nullable=False)
    elementId_2 = db.Column(db.Integer, primary_key=True, nullable=False)
    obsDatetime_2 = db.Column(db.DateTime, primary_key=True, nullable=False)
    obsValue_2 = db.Column(db.Integer)
    qcStatus_2 = db.Column(db.Integer)
    acquisitionType_2 = db.Column(db.Integer)
    obsLevel_2 = db.Column(db.String(50))
    capturedBy_2 = db.Column(db.String(50))
    dataForm_2 = db.Column(db.String(50))



class QcInterelementRelationshipDefinition(db_Model):
    __tablename__ = 'qc_interelement_relationship_definition'

    elementId_1 = db.Column(db.Integer, primary_key=True, nullable=False)
    relationship = db.Column(db.String(50), primary_key=True, nullable=False)
    elementId_2 = db.Column(db.Integer, primary_key=True, nullable=False)



class Qcstatusdefinition(db_Model):
    __tablename__ = 'qcstatusdefinition'

    code = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    description = db.Column(db.String(255))



class Qctype(db_Model):
    __tablename__ = 'qctype'

    code = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    description = db.Column(db.String(255))



class Regkey(db_Model):
    __tablename__ = 'regkeys'

    keyName = db.Column(db.String(255), primary_key=True, server_default=db.FetchedValue())
    keyValue = db.Column(db.String(255))
    keyDescription = db.Column(db.String(255))



class SeqDailyElement(db_Model):
    __tablename__ = 'seq_daily_element'

    seq = db.Column(db.BigInteger, primary_key=True)
    elementId = db.Column(db.BigInteger, nullable=False)



t_seq_day = db_Table(
    'seq_day',
    db.Column('dd', db.String(50), server_default=db.FetchedValue())
)



class SeqElement(db_Model):
    __tablename__ = 'seq_element'

    seq = db.Column(db.BigInteger, primary_key=True, index=True)
    element_code = db.Column(db.String(50))



t_seq_hour = db_Table(
    'seq_hour',
    db.Column('hh', db.Integer, server_default=db.FetchedValue())
)



t_seq_leap_year = db_Table(
    'seq_leap_year',
    db.Column('yyyy', db.Integer)
)



t_seq_month = db_Table(
    'seq_month',
    db.Column('mm', db.String(50), server_default=db.FetchedValue())
)



class SeqMonthDay(db_Model):
    __tablename__ = 'seq_month_day'

    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)



t_seq_month_day_element = db_Table(
    'seq_month_day_element',
    db.Column('mm', db.Integer, nullable=False),
    db.Column('dd', db.Integer, nullable=False),
    db.Column('elementId', db.Integer, nullable=False)
)



t_seq_month_day_element_leap_yr = db_Table(
    'seq_month_day_element_leap_yr',
    db.Column('mm', db.Integer, nullable=False),
    db.Column('dd', db.Integer, nullable=False),
    db.Column('elementId', db.Integer, nullable=False)
)



class SeqMonthDayLeapYr(db_Model):
    __tablename__ = 'seq_month_day_leap_yr'

    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)



class SeqMonthDaySynoptime(db_Model):
    __tablename__ = 'seq_month_day_synoptime'

    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)
    hh = db.Column(db.Integer, primary_key=True, nullable=False)



class SeqMonthDaySynoptimeLeapYr(db_Model):
    __tablename__ = 'seq_month_day_synoptime_leap_yr'

    mm = db.Column(db.Integer, primary_key=True, nullable=False)
    dd = db.Column(db.Integer, primary_key=True, nullable=False)
    hh = db.Column(db.Integer, primary_key=True, nullable=False)



class SeqMonthlyElement(db_Model):
    __tablename__ = 'seq_monthly_element'

    seq = db.Column(db.BigInteger, primary_key=True)
    elementId = db.Column(db.BigInteger, nullable=False)



t_seq_year = db_Table(
    'seq_year',
    db.Column('yyyy', db.Integer)
)



class Station(db_Model):
    __tablename__ = 'station'
#    __bind_key__ = 'climsoft4_prod'

    stationId = db.Column(db.String(255), primary_key=True, index=True)
    stationName = db.Column(db.String(255))
    wmoid = db.Column(db.String(20))
    icaoid = db.Column(db.String(20))
    latitude = db.Column(db.Float(11, True))
    qualifier = db.Column(db.String(20))
    longitude = db.Column(db.Float(11, True))
    elevation = db.Column(db.String(255))
    geoLocationMethod = db.Column(db.String(255))
    geoLocationAccuracy = db.Column(db.Float(11))
    openingDatetime = db.Column(db.String(50))
    closingDatetime = db.Column(db.String(50))
    country = db.Column(db.String(50))
    authority = db.Column(db.String(255))
    adminRegion = db.Column(db.String(255))
    drainageBasin = db.Column(db.String(255))
    wacaSelection = db.Column(db.Integer, server_default=db.FetchedValue())
    cptSelection = db.Column(db.Integer, server_default=db.FetchedValue())
    stationOperational = db.Column(db.Integer, server_default=db.FetchedValue())



t_stationelement = db_Table(
    'stationelement',
    db.Column('recordedFrom', db.ForeignKey('station.stationId'), index=True),
    db.Column('describedBy', db.ForeignKey('obselement.elementId'), index=True),
    db.Column('recordedWith', db.ForeignKey('instrument.instrumentId'), index=True),
    db.Column('instrumentcode', db.String(6)),
    db.Column('scheduledFor', db.ForeignKey('obsscheduleclass.scheduleClass'), index=True),
    db.Column('height', db.Float(6)),
    db.Column('beginDate', db.String(50)),
    db.Column('endDate', db.String(50)),
    db.Index('stationElementIdentification', 'recordedFrom', 'describedBy', 'recordedWith', 'beginDate')
)



t_stationidalias = db_Table(
    'stationidalias',
    db.Column('idAlias', db.String(255), unique=True),
    db.Column('refersTo', db.String(255)),
    db.Column('belongsTo', db.ForeignKey('station.stationId'), index=True),
    db.Column('idAliasBeginDate', db.String(50)),
    db.Column('idAliasEndDate', db.String(50))
)



t_stationlocationhistory = db_Table(
    'stationlocationhistory',
    db.Column('belongsTo', db.ForeignKey('station.stationId')),
    db.Column('stationType', db.String(255)),
    db.Column('geoLocationMethod', db.String(255)),
    db.Column('geoLocationAccuracy', db.Float(11)),
    db.Column('openingDatetime', db.String(50)),
    db.Column('closingDatetime', db.String(50)),
    db.Column('latitude', db.Float(11, True)),
    db.Column('longitude', db.Float(11, True)),
    db.Column('elevation', db.BigInteger),
    db.Column('authority', db.String(255)),
    db.Column('adminRegion', db.String(255)),
    db.Column('drainageBasin', db.String(255)),
    db.Index('history', 'belongsTo', 'openingDatetime')
)



class Stationnetworkdefinition(db_Model):
    __tablename__ = 'stationnetworkdefinition'

    networkAbbreviation = db.Column(db.String(255), primary_key=True, server_default=db.FetchedValue())
    networkFullName = db.Column(db.String(255))



t_stationqualifier = db_Table(
    'stationqualifier',
    db.Column('qualifier', db.String(255)),
    db.Column('qualifierBeginDate', db.String(50)),
    db.Column('qualifierEndDate', db.String(50)),
    db.Column('stationTimeZone', db.Integer, server_default=db.FetchedValue()),
    db.Column('stationNetworkType', db.String(255)),
    db.Column('belongsTo', db.ForeignKey('station.stationId'), index=True),
    db.Index('stationid_qualifier_identification', 'qualifier', 'qualifierBeginDate', 'qualifierEndDate', 'belongsTo')
)



class Synopfeature(db_Model):
    __tablename__ = 'synopfeature'

    abbreviation = db.Column(db.String(255), primary_key=True)
    description = db.Column(db.String(255))



class Tblproduct(db_Model):
    __tablename__ = 'tblproducts'

    productId = db.Column(db.String(10), primary_key=True, index=True)
    productName = db.Column(db.String(50))
    prDetails = db.Column(db.String(50))
    prCategory = db.Column(db.String(50))



t_tdcf_indicators = db_Table(
    'tdcf_indicators',
    db.Column('CREX_Edition', db.Integer, server_default=db.FetchedValue()),
    db.Column('CREX_Table', db.Integer, server_default=db.FetchedValue()),
    db.Column('BUFR_Table', db.Integer, server_default=db.FetchedValue()),
    db.Column('Local_Table', db.Integer, server_default=db.FetchedValue()),
    db.Column('Data_Category', db.Integer, server_default=db.FetchedValue()),
    db.Column('Data_SubCategory', db.Integer, server_default=db.FetchedValue()),
    db.Column('Originating_Centre', db.Integer, server_default=db.FetchedValue())
)



t_tm_307073 = db_Table(
    'tm_307073',
    db.Column('order', db.Float(asdecimal=True)),
    db.Column('Bufr_Template', db.String(255)),
    db.Column('CREX_Template', db.String(255)),
    db.Column('Sequence_Descriptor1', db.String(255)),
    db.Column('Sequence_Descriptor0', db.String(255)),
    db.Column('Bufr_Element', db.String(255)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('Crex_Unit', db.String(255)),
    db.Column('Crex_Scale', db.String(255)),
    db.Column('Crex_DataWidth', db.String(255)),
    db.Column('Bufr_Unit', db.String(255)),
    db.Column('Bufr_Scale', db.Float(asdecimal=True)),
    db.Column('Bufr_RefValue', db.Float(asdecimal=True)),
    db.Column('Bufr_DataWidth_Bits', db.Float(asdecimal=True)),
    db.Column('Selected', db.Integer),
    db.Column('Observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(255))
)



t_tm_307080 = db_Table(
    'tm_307080',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('synop_code', db.String(255), index=True),
    db.Column('unit', db.String(255)),
    db.Column('scale', db.String(255)),
    db.Column('width', db.String(255)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



t_tm_307081 = db_Table(
    'tm_307081',
    db.Column('Nos', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('synop_code', db.String(255), index=True),
    db.Column('unit', db.String(255)),
    db.Column('scale', db.String(255)),
    db.Column('width', db.String(255)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('Observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



t_tm_307082 = db_Table(
    'tm_307082',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('synop_code', db.String(255), index=True),
    db.Column('unit', db.String(255)),
    db.Column('scale', db.String(255)),
    db.Column('width', db.String(255)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



t_tm_307083 = db_Table(
    'tm_307083',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('synop_code', db.String(255), index=True),
    db.Column('unit', db.String(255)),
    db.Column('scale', db.String(255)),
    db.Column('width', db.String(255)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



t_tm_307084 = db_Table(
    'tm_307084',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('synop_code', db.String(255), index=True),
    db.Column('unit', db.String(255)),
    db.Column('scale', db.String(255)),
    db.Column('width', db.String(255)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



t_tm_307086 = db_Table(
    'tm_307086',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(50)),
    db.Column('Sequence_Descriptor0', db.String(50)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(255)),
    db.Column('Element_Name', db.String(255)),
    db.Column('synop_code', db.String(255), index=True),
    db.Column('unit', db.String(255)),
    db.Column('scale', db.String(255)),
    db.Column('width', db.String(255)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('observation', db.String(255)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



t_tm_307089 = db_Table(
    'tm_307089',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('Crex_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(10)),
    db.Column('Sequence_Descriptor0', db.String(10)),
    db.Column('Bufr_Element', db.String(50)),
    db.Column('Crex_Element', db.String(255)),
    db.Column('Climsoft_Element', db.String(50)),
    db.Column('Element_Name', db.String(255), index=True),
    db.Column('synop_code', db.String(50), index=True),
    db.Column('unit', db.String(50)),
    db.Column('scale', db.String(50)),
    db.Column('width', db.String(50)),
    db.Column('units_length_scale', db.String(255)),
    db.Column('data_type', db.String(255)),
    db.Column('selected', db.Integer),
    db.Column('observation', db.String(100)),
    db.Column('crex', db.String(25)),
    db.Column('Crex_Data', db.String(255)),
    db.Column('Bufr_Data', db.String(50))
)



class Tm307091(db_Model):
    __tablename__ = 'tm_307091'

    Rec = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    Bufr_Template = db.Column(db.String(50))
    CREX_Template = db.Column(db.String(50))
    Sequence_Descriptor1 = db.Column(db.String(255))
    Sequence_Descriptor0 = db.Column(db.String(255))
    Bufr_Element = db.Column(db.String(255))
    Crex_Element = db.Column(db.String(50))
    Climsoft_Element = db.Column(db.String(50))
    Element_Name = db.Column(db.String(255))
    Crex_Unit = db.Column(db.String(25))
    Crex_Scale = db.Column(db.String(25))
    Crex_DataWidth = db.Column(db.String(25))
    Bufr_Unit = db.Column(db.String(255))
    Bufr_Scale = db.Column(db.Integer)
    Bufr_RefValue = db.Column(db.BigInteger)
    Bufr_DataWidth_Bits = db.Column(db.Integer)
    Selected = db.Column(db.Integer)
    Observation = db.Column(db.String(255))
    Crex_Data = db.Column(db.String(30))
    Bufr_Data = db.Column(db.String(255))



t_tm_307092 = db_Table(
    'tm_307092',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('CREX_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(255)),
    db.Column('Sequence_Descriptor0', db.String(255)),
    db.Column('Bufr_Element', db.String(255)),
    db.Column('Crex_Element', db.String(50)),
    db.Column('Climsoft_Element', db.String(50)),
    db.Column('Element_Name', db.String(255)),
    db.Column('Crex_Unit', db.String(25)),
    db.Column('Crex_Scale', db.String(25)),
    db.Column('Crex_DataWidth', db.String(25)),
    db.Column('Bufr_Unit', db.String(255)),
    db.Column('Bufr_Scale', db.Integer),
    db.Column('Bufr_RefValue', db.BigInteger),
    db.Column('Bufr_DataWidth_Bits', db.Integer),
    db.Column('Selected', db.Integer),
    db.Column('Observation', db.String(255)),
    db.Column('Crex_Data', db.String(30)),
    db.Column('Bufr_Data', db.String(255))
)



t_tm_309052 = db_Table(
    'tm_309052',
    db.Column('order', db.Integer, server_default=db.FetchedValue()),
    db.Column('Bufr_Template', db.String(50)),
    db.Column('CREX_Template', db.String(50)),
    db.Column('Sequence_Descriptor1', db.String(255)),
    db.Column('Sequence_Descriptor0', db.String(255)),
    db.Column('Bufr_Element', db.String(255)),
    db.Column('Crex_Element', db.String(50)),
    db.Column('Climsoft_Element', db.String(50)),
    db.Column('Element_Name', db.String(255)),
    db.Column('Crex_Unit', db.String(25)),
    db.Column('Crex_Scale', db.String(25)),
    db.Column('Crex_DataWidth', db.String(25)),
    db.Column('Bufr_Unit', db.String(255)),
    db.Column('Bufr_Scale', db.Integer),
    db.Column('Bufr_RefValue', db.BigInteger),
    db.Column('Bufr_DataWidth_Bits', db.Integer),
    db.Column('Selected', db.Integer),
    db.Column('Observation', db.String(255)),
    db.Column('Crex_Data', db.String(30)),
    db.Column('Bufr_Data', db.String(255))
)



class Userrecord(db_Model):
    __tablename__ = 'userrecords'

    username = db.Column(db.String(255), primary_key=True, server_default=db.FetchedValue())
    recsdone = db.Column(db.Integer)
    recsexpt = db.Column(db.Integer)
    perform = db.Column(db.Integer)
