# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class MdlConfig(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField()
    class Meta:
        db_table = u'mdl_config'

class MdlConfigPlugins(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    plugin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    value = models.TextField()
    class Meta:
        db_table = u'mdl_config_plugins'

class MdlCourse(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    category = models.TextField() # This field type is a guess.
    sortorder = models.TextField() # This field type is a guess.
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField()
    format = models.CharField(max_length=10)
    showgrades = models.SmallIntegerField()
    modinfo = models.TextField()
    newsitems = models.IntegerField()
    teacher = models.CharField(max_length=100)
    teachers = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
    students = models.CharField(max_length=100)
    guest = models.SmallIntegerField()
    startdate = models.TextField() # This field type is a guess.
    enrolperiod = models.TextField() # This field type is a guess.
    numsections = models.IntegerField()
    marker = models.TextField() # This field type is a guess.
    maxbytes = models.TextField() # This field type is a guess.
    showreports = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    hiddensections = models.SmallIntegerField()
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.TextField() # This field type is a guess.
    lang = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    cost = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    metacourse = models.SmallIntegerField()
    requested = models.SmallIntegerField()
    restrictmodules = models.SmallIntegerField()
    expirynotify = models.SmallIntegerField()
    expirythreshold = models.TextField() # This field type is a guess.
    notifystudents = models.SmallIntegerField()
    enrollable = models.SmallIntegerField()
    enrolstartdate = models.TextField() # This field type is a guess.
    enrolenddate = models.TextField() # This field type is a guess.
    enrol = models.CharField(max_length=20)
    defaultrole = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_course'

class MdlCourseCategories(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.TextField() # This field type is a guess.
    sortorder = models.TextField() # This field type is a guess.
    coursecount = models.TextField() # This field type is a guess.
    visible = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    depth = models.TextField() # This field type is a guess.
    path = models.CharField(max_length=255)
    theme = models.CharField(max_length=50)
    class Meta:
        db_table = u'mdl_course_categories'

class MdlCourseDisplay(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    display = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_course_display'

class MdlCourseMeta(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    parent_course = models.TextField() # This field type is a guess.
    child_course = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_course_meta'

class MdlCourseModules(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    module = models.TextField() # This field type is a guess.
    instance = models.TextField() # This field type is a guess.
    section = models.TextField() # This field type is a guess.
    idnumber = models.CharField(max_length=100)
    added = models.TextField() # This field type is a guess.
    score = models.SmallIntegerField()
    indent = models.IntegerField()
    visible = models.SmallIntegerField()
    visibleold = models.SmallIntegerField()
    groupmode = models.SmallIntegerField()
    groupingid = models.TextField() # This field type is a guess.
    groupmembersonly = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_course_modules'

class MdlCourseSections(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    section = models.TextField() # This field type is a guess.
    summary = models.TextField()
    sequence = models.TextField()
    visible = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_course_sections'

class MdlCourseRequest(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=15)
    summary = models.TextField()
    reason = models.TextField()
    requester = models.TextField() # This field type is a guess.
    password = models.CharField(max_length=50)
    class Meta:
        db_table = u'mdl_course_request'

class MdlCourseAllowedModules(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    module = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_course_allowed_modules'

class MdlEvent(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=255)
    description = models.TextField()
    format = models.SmallIntegerField()
    courseid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    repeatid = models.TextField() # This field type is a guess.
    modulename = models.CharField(max_length=20)
    instance = models.TextField() # This field type is a guess.
    eventtype = models.CharField(max_length=20)
    timestart = models.TextField() # This field type is a guess.
    timeduration = models.TextField() # This field type is a guess.
    visible = models.SmallIntegerField()
    uuid = models.CharField(max_length=36)
    sequence = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_event'

class MdlCacheFilters(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    filter = models.CharField(max_length=32)
    version = models.TextField() # This field type is a guess.
    md5key = models.CharField(max_length=32)
    rawtext = models.TextField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_cache_filters'

class MdlCacheText(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    md5key = models.CharField(max_length=32)
    formattedtext = models.TextField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_cache_text'

class MdlLog(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    time = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    ip = models.CharField(max_length=15)
    course = models.TextField() # This field type is a guess.
    module = models.CharField(max_length=20)
    cmid = models.TextField() # This field type is a guess.
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_log'

class MdlLogDisplay(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    module = models.CharField(max_length=20)
    action = models.CharField(max_length=40)
    mtable = models.CharField(max_length=30)
    field = models.CharField(max_length=200)
    class Meta:
        db_table = u'mdl_log_display'

class MdlMessage(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    useridfrom = models.TextField() # This field type is a guess.
    useridto = models.TextField() # This field type is a guess.
    message = models.TextField()
    format = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    messagetype = models.CharField(max_length=50)
    class Meta:
        db_table = u'mdl_message'

class MdlMessageRead(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    useridfrom = models.TextField() # This field type is a guess.
    useridto = models.TextField() # This field type is a guess.
    message = models.TextField()
    format = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timeread = models.TextField() # This field type is a guess.
    messagetype = models.CharField(max_length=50)
    mailed = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_message_read'

class MdlMessageContacts(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    contactid = models.TextField() # This field type is a guess.
    blocked = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_message_contacts'

class MdlModules(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=20)
    version = models.TextField() # This field type is a guess.
    cron = models.TextField() # This field type is a guess.
    lastcron = models.TextField() # This field type is a guess.
    search = models.CharField(max_length=255)
    visible = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_modules'

class MdlSessions2(models.Model):
    sesskey = models.CharField(max_length=64, primary_key=True)
    expiry = models.DateTimeField()
    expireref = models.CharField(max_length=250)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    sessdata = models.TextField()
    class Meta:
        db_table = u'mdl_sessions2'

class AdodbLogsql(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    created = models.DateTimeField()
    sql0 = models.CharField(max_length=250)
    sql1 = models.TextField()
    params = models.TextField()
    tracer = models.TextField()
    timer = models.DecimalField(max_digits=16, decimal_places=6)
    class Meta:
        db_table = u'adodb_logsql'

class MdlTimezone(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=100)
    year = models.TextField() # This field type is a guess.
    tzrule = models.CharField(max_length=20)
    gmtoff = models.TextField() # This field type is a guess.
    dstoff = models.TextField() # This field type is a guess.
    dst_month = models.SmallIntegerField()
    dst_startday = models.SmallIntegerField()
    dst_weekday = models.SmallIntegerField()
    dst_skipweeks = models.SmallIntegerField()
    dst_time = models.CharField(max_length=6)
    std_month = models.SmallIntegerField()
    std_startday = models.SmallIntegerField()
    std_weekday = models.SmallIntegerField()
    std_skipweeks = models.SmallIntegerField()
    std_time = models.CharField(max_length=6)
    class Meta:
        db_table = u'mdl_timezone'

class MdlUser(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    auth = models.CharField(max_length=20)
    confirmed = models.SmallIntegerField()
    policyagreed = models.SmallIntegerField()
    deleted = models.SmallIntegerField()
    mnethostid = models.TextField() # This field type is a guess.
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.SmallIntegerField()
    icq = models.CharField(max_length=15)
    skype = models.CharField(max_length=50)
    yahoo = models.CharField(max_length=50)
    aim = models.CharField(max_length=50)
    msn = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=40)
    department = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.TextField() # This field type is a guess.
    lastaccess = models.TextField() # This field type is a guess.
    lastlogin = models.TextField() # This field type is a guess.
    currentlogin = models.TextField() # This field type is a guess.
    lastip = models.CharField(max_length=15)
    secret = models.CharField(max_length=15)
    picture = models.SmallIntegerField()
    url = models.CharField(max_length=255)
    description = models.TextField()
    mailformat = models.SmallIntegerField()
    maildigest = models.SmallIntegerField()
    maildisplay = models.SmallIntegerField()
    htmleditor = models.SmallIntegerField()
    ajax = models.SmallIntegerField()
    autosubscribe = models.SmallIntegerField()
    trackforums = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    trustbitmask = models.TextField() # This field type is a guess.
    imagealt = models.CharField(max_length=255)
    screenreader = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_user'

class MdlUserPreferences(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_user_preferences'

class MdlUserLastaccess(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    timeaccess = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_user_lastaccess'

class MdlScale(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_scale'

class MdlScaleHistory(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    action = models.TextField() # This field type is a guess.
    oldid = models.TextField() # This field type is a guess.
    source = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    loggeduser = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()
    class Meta:
        db_table = u'mdl_scale_history'

class MdlStatsDaily(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    stattype = models.CharField(max_length=20)
    stat1 = models.TextField() # This field type is a guess.
    stat2 = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_stats_daily'

class MdlStatsWeekly(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    stattype = models.CharField(max_length=20)
    stat1 = models.TextField() # This field type is a guess.
    stat2 = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_stats_weekly'

class MdlStatsMonthly(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    stattype = models.CharField(max_length=20)
    stat1 = models.TextField() # This field type is a guess.
    stat2 = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_stats_monthly'

class MdlStatsUserDaily(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    statsreads = models.TextField() # This field type is a guess.
    statswrites = models.TextField() # This field type is a guess.
    stattype = models.CharField(max_length=30)
    class Meta:
        db_table = u'mdl_stats_user_daily'

class MdlStatsUserWeekly(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    statsreads = models.TextField() # This field type is a guess.
    statswrites = models.TextField() # This field type is a guess.
    stattype = models.CharField(max_length=30)
    class Meta:
        db_table = u'mdl_stats_user_weekly'

class MdlStatsUserMonthly(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    statsreads = models.TextField() # This field type is a guess.
    statswrites = models.TextField() # This field type is a guess.
    stattype = models.CharField(max_length=30)
    class Meta:
        db_table = u'mdl_stats_user_monthly'

class MdlPost(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    module = models.CharField(max_length=20)
    userid = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    moduleid = models.TextField() # This field type is a guess.
    coursemoduleid = models.TextField() # This field type is a guess.
    subject = models.CharField(max_length=128)
    summary = models.TextField()
    content = models.TextField()
    uniquehash = models.CharField(max_length=128)
    rating = models.TextField() # This field type is a guess.
    format = models.TextField() # This field type is a guess.
    attachment = models.CharField(max_length=100)
    publishstate = models.CharField(max_length=20)
    lastmodified = models.TextField() # This field type is a guess.
    created = models.TextField() # This field type is a guess.
    usermodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_post'

class MdlRole(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=255)
    shortname = models.CharField(max_length=100)
    description = models.TextField()
    sortorder = models.TextField(unique=True) # This field type is a guess.
    class Meta:
        db_table = u'mdl_role'

class MdlContext(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    contextlevel = models.TextField() # This field type is a guess.
    instanceid = models.TextField() # This field type is a guess.
    path = models.CharField(max_length=255)
    depth = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_context'

class MdlCapabilities(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    captype = models.CharField(max_length=50)
    contextlevel = models.TextField() # This field type is a guess.
    component = models.CharField(max_length=100)
    riskbitmask = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_capabilities'

class MdlRoleAllowAssign(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    allowassign = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_role_allow_assign'

class MdlRoleAllowOverride(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    allowoverride = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_role_allow_override'

class MdlRoleAssignments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    contextid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    hidden = models.SmallIntegerField()
    timestart = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    modifierid = models.TextField() # This field type is a guess.
    enrol = models.CharField(max_length=20)
    sortorder = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_role_assignments'

class MdlRoleCapabilities(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    contextid = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    capability = models.CharField(max_length=255)
    permission = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    modifierid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_role_capabilities'

class MdlRoleNames(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    contextid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_role_names'

class MdlRoleSortorder(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    roleid = models.TextField() # This field type is a guess.
    contextid = models.TextField() # This field type is a guess.
    sortoder = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_role_sortorder'

class MdlContextTemp(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    path = models.CharField(max_length=255)
    depth = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_context_temp'

class MdlUserInfoField(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    shortname = models.CharField(max_length=255)
    name = models.TextField()
    datatype = models.CharField(max_length=255)
    description = models.TextField()
    categoryid = models.TextField() # This field type is a guess.
    sortorder = models.TextField() # This field type is a guess.
    required = models.SmallIntegerField()
    locked = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    forceunique = models.SmallIntegerField()
    signup = models.SmallIntegerField()
    defaultdata = models.TextField()
    param1 = models.TextField()
    param2 = models.TextField()
    param3 = models.TextField()
    param4 = models.TextField()
    param5 = models.TextField()
    class Meta:
        db_table = u'mdl_user_info_field'

class MdlUserInfoCategory(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=255)
    sortorder = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_user_info_category'

class MdlUserInfoData(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    fieldid = models.TextField() # This field type is a guess.
    data = models.TextField()
    class Meta:
        db_table = u'mdl_user_info_data'

class MdlMnetEnrolCourse(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    hostid = models.TextField() # This field type is a guess.
    remoteid = models.TextField() # This field type is a guess.
    cat_id = models.TextField() # This field type is a guess.
    cat_name = models.CharField(max_length=255)
    cat_description = models.TextField()
    sortorder = models.TextField() # This field type is a guess.
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=15)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField()
    startdate = models.TextField() # This field type is a guess.
    cost = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    defaultroleid = models.SmallIntegerField()
    defaultrolename = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_mnet_enrol_course'

class MdlMnetEnrolAssignments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    hostid = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    rolename = models.CharField(max_length=255)
    enroltime = models.TextField() # This field type is a guess.
    enroltype = models.CharField(max_length=20)
    class Meta:
        db_table = u'mdl_mnet_enrol_assignments'

class MdlMnetApplication(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    xmlrpc_server_url = models.CharField(max_length=255)
    sso_land_url = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_mnet_application'

class MdlMnetHost(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    deleted = models.SmallIntegerField()
    wwwroot = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=39)
    name = models.CharField(max_length=80)
    public_key = models.TextField()
    public_key_expires = models.TextField() # This field type is a guess.
    transport = models.SmallIntegerField()
    portno = models.SmallIntegerField()
    last_connect_time = models.TextField() # This field type is a guess.
    last_log_id = models.TextField() # This field type is a guess.
    force_theme = models.SmallIntegerField()
    theme = models.CharField(max_length=100)
    applicationid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_mnet_host'

class MdlMnetHost2Service(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    hostid = models.TextField() # This field type is a guess.
    serviceid = models.TextField() # This field type is a guess.
    publish = models.SmallIntegerField()
    subscribe = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_mnet_host2service'

class MdlMnetLog(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    hostid = models.TextField() # This field type is a guess.
    remoteid = models.TextField() # This field type is a guess.
    time = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    ip = models.CharField(max_length=15)
    course = models.TextField() # This field type is a guess.
    coursename = models.CharField(max_length=40)
    module = models.CharField(max_length=20)
    cmid = models.TextField() # This field type is a guess.
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_mnet_log'

class MdlMnetRpc(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    function_name = models.CharField(max_length=40)
    xmlrpc_path = models.CharField(max_length=80)
    parent_type = models.CharField(max_length=6)
    parent = models.CharField(max_length=20)
    enabled = models.SmallIntegerField()
    help = models.TextField()
    profile = models.TextField()
    class Meta:
        db_table = u'mdl_mnet_rpc'

class MdlMnetService(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    apiversion = models.CharField(max_length=10)
    offer = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_mnet_service'

class MdlMnetService2Rpc(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    serviceid = models.TextField() # This field type is a guess.
    rpcid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_mnet_service2rpc'

class MdlMnetSession(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    username = models.CharField(max_length=100)
    token = models.CharField(unique=True, max_length=40)
    mnethostid = models.TextField() # This field type is a guess.
    useragent = models.CharField(max_length=40)
    confirm_timeout = models.TextField() # This field type is a guess.
    session_id = models.CharField(max_length=40)
    expires = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_mnet_session'

class MdlMnetSsoAccessControl(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    username = models.CharField(max_length=100)
    mnet_host_id = models.TextField() # This field type is a guess.
    accessctrl = models.CharField(max_length=20)
    class Meta:
        db_table = u'mdl_mnet_sso_access_control'

class MdlEventsQueue(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    eventdata = models.TextField()
    stackdump = models.TextField()
    userid = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_events_queue'

class MdlEventsHandlers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    eventname = models.CharField(max_length=166)
    handlermodule = models.CharField(max_length=166)
    handlerfile = models.CharField(max_length=255)
    handlerfunction = models.TextField()
    schedule = models.CharField(max_length=255)
    status = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_events_handlers'

class MdlEventsQueueHandlers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    queuedeventid = models.TextField() # This field type is a guess.
    handlerid = models.TextField() # This field type is a guess.
    status = models.TextField() # This field type is a guess.
    errormessage = models.TextField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_events_queue_handlers'

class MdlGradeOutcomes(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.TextField() # This field type is a guess.
    description = models.TextField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    usermodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_outcomes'

class MdlGradeOutcomesCourses(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    outcomeid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_outcomes_courses'

class MdlGradeCategories(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    parent = models.TextField() # This field type is a guess.
    depth = models.TextField() # This field type is a guess.
    path = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    aggregation = models.TextField() # This field type is a guess.
    keephigh = models.TextField() # This field type is a guess.
    droplow = models.TextField() # This field type is a guess.
    aggregateonlygraded = models.SmallIntegerField()
    aggregateoutcomes = models.SmallIntegerField()
    aggregatesubcats = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_categories'

class MdlGradeItems(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    categoryid = models.TextField() # This field type is a guess.
    itemname = models.CharField(max_length=255)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30)
    iteminstance = models.TextField() # This field type is a guess.
    itemnumber = models.TextField() # This field type is a guess.
    iteminfo = models.TextField()
    idnumber = models.CharField(max_length=255)
    calculation = models.TextField()
    gradetype = models.SmallIntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.TextField() # This field type is a guess.
    outcomeid = models.TextField() # This field type is a guess.
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.TextField() # This field type is a guess.
    display = models.TextField() # This field type is a guess.
    decimals = models.SmallIntegerField()
    hidden = models.TextField() # This field type is a guess.
    locked = models.TextField() # This field type is a guess.
    locktime = models.TextField() # This field type is a guess.
    needsupdate = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_items'

class MdlGradeGrades(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    itemid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.TextField() # This field type is a guess.
    usermodified = models.TextField() # This field type is a guess.
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5)
    hidden = models.TextField() # This field type is a guess.
    locked = models.TextField() # This field type is a guess.
    locktime = models.TextField() # This field type is a guess.
    exported = models.TextField() # This field type is a guess.
    overridden = models.TextField() # This field type is a guess.
    excluded = models.TextField() # This field type is a guess.
    feedback = models.TextField()
    feedbackformat = models.TextField() # This field type is a guess.
    information = models.TextField()
    informationformat = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_grades'

class MdlGradeOutcomesHistory(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    action = models.TextField() # This field type is a guess.
    oldid = models.TextField() # This field type is a guess.
    source = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    loggeduser = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.TextField() # This field type is a guess.
    description = models.TextField()
    class Meta:
        db_table = u'mdl_grade_outcomes_history'

class MdlGradeCategoriesHistory(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    action = models.TextField() # This field type is a guess.
    oldid = models.TextField() # This field type is a guess.
    source = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    loggeduser = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    parent = models.TextField() # This field type is a guess.
    depth = models.TextField() # This field type is a guess.
    path = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    aggregation = models.TextField() # This field type is a guess.
    keephigh = models.TextField() # This field type is a guess.
    droplow = models.TextField() # This field type is a guess.
    aggregateonlygraded = models.SmallIntegerField()
    aggregateoutcomes = models.SmallIntegerField()
    aggregatesubcats = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_grade_categories_history'

class MdlGradeItemsHistory(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    action = models.TextField() # This field type is a guess.
    oldid = models.TextField() # This field type is a guess.
    source = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    loggeduser = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    categoryid = models.TextField() # This field type is a guess.
    itemname = models.CharField(max_length=255)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30)
    iteminstance = models.TextField() # This field type is a guess.
    itemnumber = models.TextField() # This field type is a guess.
    iteminfo = models.TextField()
    idnumber = models.CharField(max_length=255)
    calculation = models.TextField()
    gradetype = models.SmallIntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.TextField() # This field type is a guess.
    outcomeid = models.TextField() # This field type is a guess.
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.TextField() # This field type is a guess.
    hidden = models.TextField() # This field type is a guess.
    locked = models.TextField() # This field type is a guess.
    locktime = models.TextField() # This field type is a guess.
    needsupdate = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_items_history'

class MdlGradeGradesHistory(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    action = models.TextField() # This field type is a guess.
    oldid = models.TextField() # This field type is a guess.
    source = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    loggeduser = models.TextField() # This field type is a guess.
    itemid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.TextField() # This field type is a guess.
    usermodified = models.TextField() # This field type is a guess.
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5)
    hidden = models.TextField() # This field type is a guess.
    locked = models.TextField() # This field type is a guess.
    locktime = models.TextField() # This field type is a guess.
    exported = models.TextField() # This field type is a guess.
    overridden = models.TextField() # This field type is a guess.
    excluded = models.TextField() # This field type is a guess.
    feedback = models.TextField()
    feedbackformat = models.TextField() # This field type is a guess.
    information = models.TextField()
    informationformat = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_grades_history'

class MdlGradeImportNewitem(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    itemname = models.CharField(max_length=255)
    importcode = models.TextField() # This field type is a guess.
    importer = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_import_newitem'

class MdlGradeImportValues(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    itemid = models.TextField() # This field type is a guess.
    newgradeitem = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5)
    feedback = models.TextField()
    importcode = models.TextField() # This field type is a guess.
    importer = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_grade_import_values'

class MdlTag(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    rawname = models.CharField(max_length=255)
    tagtype = models.CharField(max_length=255)
    description = models.TextField()
    descriptionformat = models.SmallIntegerField()
    flag = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_tag'

class MdlTagCorrelation(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    tagid = models.TextField() # This field type is a guess.
    correlatedtags = models.TextField()
    class Meta:
        db_table = u'mdl_tag_correlation'

class MdlTagInstance(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    tagid = models.TextField() # This field type is a guess.
    itemtype = models.CharField(max_length=255)
    itemid = models.TextField() # This field type is a guess.
    ordering = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_tag_instance'

class MdlGroups(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=254)
    description = models.TextField()
    enrolmentkey = models.CharField(max_length=50)
    picture = models.TextField() # This field type is a guess.
    hidepicture = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_groups'

class MdlGroupings(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    description = models.TextField()
    configdata = models.TextField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_groupings'

class MdlGroupsMembers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    timeadded = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_groups_members'

class MdlGroupingsGroups(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    groupingid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    timeadded = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_groupings_groups'

class MdlUserPrivateKey(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    script = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    userid = models.TextField() # This field type is a guess.
    instance = models.TextField() # This field type is a guess.
    iprestriction = models.CharField(max_length=255)
    validuntil = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_user_private_key'

class MdlGradeLetters(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    contextid = models.TextField() # This field type is a guess.
    lowerboundary = models.DecimalField(max_digits=10, decimal_places=5)
    letter = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_grade_letters'

class MdlCacheFlags(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    flagtype = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    value = models.TextField()
    expiry = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_cache_flags'

class MdlGradeSettings(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    value = models.TextField()
    class Meta:
        db_table = u'mdl_grade_settings'

class MdlWebdavLocks(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    token = models.CharField(unique=True, max_length=255)
    path = models.CharField(max_length=255)
    expiry = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    recursive = models.SmallIntegerField()
    exclusivelock = models.SmallIntegerField()
    created = models.TextField() # This field type is a guess.
    modified = models.TextField() # This field type is a guess.
    owner = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_webdav_locks'

class MdlAssignment(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    description = models.TextField()
    format = models.SmallIntegerField()
    assignmenttype = models.CharField(max_length=50)
    resubmit = models.SmallIntegerField()
    preventlate = models.SmallIntegerField()
    emailteachers = models.SmallIntegerField()
    var1 = models.TextField() # This field type is a guess.
    var2 = models.TextField() # This field type is a guess.
    var3 = models.TextField() # This field type is a guess.
    var4 = models.TextField() # This field type is a guess.
    var5 = models.TextField() # This field type is a guess.
    maxbytes = models.TextField() # This field type is a guess.
    timedue = models.TextField() # This field type is a guess.
    timeavailable = models.TextField() # This field type is a guess.
    grade = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_assignment'

class MdlAssignmentSubmissions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    assignment = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    numfiles = models.TextField() # This field type is a guess.
    data1 = models.TextField()
    data2 = models.TextField()
    grade = models.TextField() # This field type is a guess.
    submissioncomment = models.TextField()
    format = models.SmallIntegerField()
    teacher = models.TextField() # This field type is a guess.
    timemarked = models.TextField() # This field type is a guess.
    mailed = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_assignment_submissions'

class MdlChat(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    intro = models.TextField()
    keepdays = models.TextField() # This field type is a guess.
    studentlogs = models.SmallIntegerField()
    chattime = models.TextField() # This field type is a guess.
    schedule = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_chat'

class MdlChatMessages(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    chatid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    system = models.SmallIntegerField()
    message = models.TextField()
    timestamp = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_chat_messages'

class MdlChatUsers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    chatid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    version = models.CharField(max_length=16)
    ip = models.CharField(max_length=15)
    firstping = models.TextField() # This field type is a guess.
    lastping = models.TextField() # This field type is a guess.
    lastmessageping = models.TextField() # This field type is a guess.
    sid = models.CharField(max_length=32)
    course = models.TextField() # This field type is a guess.
    lang = models.CharField(max_length=30)
    class Meta:
        db_table = u'mdl_chat_users'

class MdlChoice(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    text = models.TextField()
    format = models.SmallIntegerField()
    publish = models.SmallIntegerField()
    showresults = models.SmallIntegerField()
    display = models.SmallIntegerField()
    allowupdate = models.SmallIntegerField()
    showunanswered = models.SmallIntegerField()
    limitanswers = models.SmallIntegerField()
    timeopen = models.TextField() # This field type is a guess.
    timeclose = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_choice'

class MdlChoiceOptions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    choiceid = models.TextField() # This field type is a guess.
    text = models.TextField()
    maxanswers = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_choice_options'

class MdlChoiceAnswers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    choiceid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    optionid = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_choice_answers'

class MdlData(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    intro = models.TextField()
    comments = models.SmallIntegerField()
    timeavailablefrom = models.TextField() # This field type is a guess.
    timeavailableto = models.TextField() # This field type is a guess.
    timeviewfrom = models.TextField() # This field type is a guess.
    timeviewto = models.TextField() # This field type is a guess.
    requiredentries = models.IntegerField()
    requiredentriestoview = models.IntegerField()
    maxentries = models.IntegerField()
    rssarticles = models.SmallIntegerField()
    singletemplate = models.TextField()
    listtemplate = models.TextField()
    listtemplateheader = models.TextField()
    listtemplatefooter = models.TextField()
    addtemplate = models.TextField()
    rsstemplate = models.TextField()
    rsstitletemplate = models.TextField()
    csstemplate = models.TextField()
    jstemplate = models.TextField()
    asearchtemplate = models.TextField()
    approval = models.SmallIntegerField()
    scale = models.TextField() # This field type is a guess.
    assessed = models.TextField() # This field type is a guess.
    defaultsort = models.TextField() # This field type is a guess.
    defaultsortdir = models.SmallIntegerField()
    editany = models.SmallIntegerField()
    notification = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_data'

class MdlDataFields(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    dataid = models.TextField() # This field type is a guess.
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    param1 = models.TextField()
    param2 = models.TextField()
    param3 = models.TextField()
    param4 = models.TextField()
    param5 = models.TextField()
    param6 = models.TextField()
    param7 = models.TextField()
    param8 = models.TextField()
    param9 = models.TextField()
    param10 = models.TextField()
    class Meta:
        db_table = u'mdl_data_fields'

class MdlDataRecords(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    dataid = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    approved = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_data_records'

class MdlDataContent(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    fieldid = models.TextField() # This field type is a guess.
    recordid = models.TextField() # This field type is a guess.
    content = models.TextField()
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    class Meta:
        db_table = u'mdl_data_content'

class MdlDataComments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    recordid = models.TextField() # This field type is a guess.
    content = models.TextField()
    format = models.SmallIntegerField()
    created = models.TextField() # This field type is a guess.
    modified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_data_comments'

class MdlDataRatings(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    recordid = models.TextField() # This field type is a guess.
    rating = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_data_ratings'

class MdlForum(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    intro = models.TextField()
    assessed = models.TextField() # This field type is a guess.
    assesstimestart = models.TextField() # This field type is a guess.
    assesstimefinish = models.TextField() # This field type is a guess.
    scale = models.TextField() # This field type is a guess.
    maxbytes = models.TextField() # This field type is a guess.
    forcesubscribe = models.SmallIntegerField()
    trackingtype = models.SmallIntegerField()
    rsstype = models.SmallIntegerField()
    rssarticles = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    warnafter = models.TextField() # This field type is a guess.
    blockafter = models.TextField() # This field type is a guess.
    blockperiod = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum'

class MdlForumDiscussions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    forum = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    firstpost = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    assessed = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    usermodified = models.TextField() # This field type is a guess.
    timestart = models.TextField() # This field type is a guess.
    timeend = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum_discussions'

class MdlForumPosts(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    discussion = models.TextField() # This field type is a guess.
    parent = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    created = models.TextField() # This field type is a guess.
    modified = models.TextField() # This field type is a guess.
    mailed = models.SmallIntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    format = models.SmallIntegerField()
    attachment = models.CharField(max_length=100)
    totalscore = models.SmallIntegerField()
    mailnow = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum_posts'

class MdlForumQueue(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    discussionid = models.TextField() # This field type is a guess.
    postid = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum_queue'

class MdlForumRatings(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    post = models.TextField() # This field type is a guess.
    time = models.TextField() # This field type is a guess.
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_forum_ratings'

class MdlForumSubscriptions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    forum = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum_subscriptions'

class MdlForumRead(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    forumid = models.TextField() # This field type is a guess.
    discussionid = models.TextField() # This field type is a guess.
    postid = models.TextField() # This field type is a guess.
    firstread = models.TextField() # This field type is a guess.
    lastread = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum_read'

class MdlForumTrackPrefs(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    forumid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_forum_track_prefs'

class MdlGlossary(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    intro = models.TextField()
    allowduplicatedentries = models.SmallIntegerField()
    displayformat = models.CharField(max_length=50)
    mainglossary = models.SmallIntegerField()
    showspecial = models.SmallIntegerField()
    showalphabet = models.SmallIntegerField()
    showall = models.SmallIntegerField()
    allowcomments = models.SmallIntegerField()
    allowprintview = models.SmallIntegerField()
    usedynalink = models.SmallIntegerField()
    defaultapproval = models.SmallIntegerField()
    globalglossary = models.SmallIntegerField()
    entbypage = models.SmallIntegerField()
    editalways = models.SmallIntegerField()
    rsstype = models.SmallIntegerField()
    rssarticles = models.SmallIntegerField()
    assessed = models.TextField() # This field type is a guess.
    assesstimestart = models.TextField() # This field type is a guess.
    assesstimefinish = models.TextField() # This field type is a guess.
    scale = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_glossary'

class MdlGlossaryEntries(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    glossaryid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    concept = models.CharField(max_length=255)
    definition = models.TextField()
    format = models.SmallIntegerField()
    attachment = models.CharField(max_length=100)
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    teacherentry = models.SmallIntegerField()
    sourceglossaryid = models.TextField() # This field type is a guess.
    usedynalink = models.SmallIntegerField()
    casesensitive = models.SmallIntegerField()
    fullmatch = models.SmallIntegerField()
    approved = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_glossary_entries'

class MdlGlossaryAlias(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    entryid = models.TextField() # This field type is a guess.
    alias = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_glossary_alias'

class MdlGlossaryCategories(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    glossaryid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    usedynalink = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_glossary_categories'

class MdlGlossaryEntriesCategories(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    categoryid = models.TextField() # This field type is a guess.
    entryid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_glossary_entries_categories'

class MdlGlossaryComments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    entryid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    entrycomment = models.TextField()
    format = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_glossary_comments'

class MdlGlossaryFormats(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=50)
    popupformatname = models.CharField(max_length=50)
    visible = models.SmallIntegerField()
    showgroup = models.SmallIntegerField()
    defaultmode = models.CharField(max_length=50)
    defaulthook = models.CharField(max_length=50)
    sortkey = models.CharField(max_length=50)
    sortorder = models.CharField(max_length=50)
    class Meta:
        db_table = u'mdl_glossary_formats'

class MdlGlossaryRatings(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    entryid = models.TextField() # This field type is a guess.
    time = models.TextField() # This field type is a guess.
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_glossary_ratings'

class MdlHotpot(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    summary = models.TextField()
    timeopen = models.TextField() # This field type is a guess.
    timeclose = models.TextField() # This field type is a guess.
    location = models.SmallIntegerField()
    reference = models.CharField(max_length=255)
    outputformat = models.SmallIntegerField()
    navigation = models.SmallIntegerField()
    studentfeedback = models.SmallIntegerField()
    studentfeedbackurl = models.CharField(max_length=255)
    forceplugins = models.SmallIntegerField()
    shownextquiz = models.SmallIntegerField()
    review = models.SmallIntegerField()
    grade = models.TextField() # This field type is a guess.
    grademethod = models.SmallIntegerField()
    attempts = models.IntegerField()
    password = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)
    clickreporting = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_hotpot'

class MdlHotpotAttempts(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    hotpot = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    starttime = models.TextField() # This field type is a guess.
    endtime = models.TextField() # This field type is a guess.
    score = models.IntegerField()
    penalties = models.IntegerField()
    attempt = models.IntegerField()
    timestart = models.TextField() # This field type is a guess.
    timefinish = models.TextField() # This field type is a guess.
    status = models.SmallIntegerField()
    clickreportid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_hotpot_attempts'

class MdlHotpotDetails(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    attempt = models.TextField() # This field type is a guess.
    details = models.TextField()
    class Meta:
        db_table = u'mdl_hotpot_details'

class MdlHotpotQuestions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.TextField()
    type = models.SmallIntegerField()
    text = models.TextField() # This field type is a guess.
    hotpot = models.TextField() # This field type is a guess.
    md5key = models.CharField(max_length=32)
    class Meta:
        db_table = u'mdl_hotpot_questions'

class MdlHotpotResponses(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    attempt = models.TextField() # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    score = models.IntegerField()
    weighting = models.IntegerField()
    correct = models.CharField(max_length=255)
    wrong = models.CharField(max_length=255)
    ignored = models.CharField(max_length=255)
    hints = models.IntegerField()
    clues = models.IntegerField()
    checks = models.IntegerField()
    class Meta:
        db_table = u'mdl_hotpot_responses'

class MdlHotpotStrings(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    string = models.TextField()
    md5key = models.CharField(max_length=32)
    class Meta:
        db_table = u'mdl_hotpot_strings'

class MdlJournal(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    days = models.IntegerField()
    assessed = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_journal'

class MdlJournalEntries(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    journal = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    modified = models.TextField() # This field type is a guess.
    text = models.TextField()
    format = models.SmallIntegerField()
    rating = models.TextField() # This field type is a guess.
    entrycomment = models.TextField()
    teacher = models.TextField() # This field type is a guess.
    timemarked = models.TextField() # This field type is a guess.
    mailed = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_journal_entries'

class MdlLabel(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    content = models.TextField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_label'

class MdlLams(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    introduction = models.TextField()
    learning_session_id = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lams'

class MdlLesson(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    practice = models.SmallIntegerField()
    modattempts = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    dependency = models.TextField() # This field type is a guess.
    conditions = models.TextField()
    grade = models.SmallIntegerField()
    custom = models.SmallIntegerField()
    ongoing = models.SmallIntegerField()
    usemaxgrade = models.SmallIntegerField()
    maxanswers = models.SmallIntegerField()
    maxattempts = models.SmallIntegerField()
    review = models.SmallIntegerField()
    nextpagedefault = models.SmallIntegerField()
    feedback = models.SmallIntegerField()
    minquestions = models.SmallIntegerField()
    maxpages = models.SmallIntegerField()
    timed = models.SmallIntegerField()
    maxtime = models.TextField() # This field type is a guess.
    retake = models.SmallIntegerField()
    activitylink = models.TextField() # This field type is a guess.
    mediafile = models.CharField(max_length=255)
    mediaheight = models.TextField() # This field type is a guess.
    mediawidth = models.TextField() # This field type is a guess.
    mediaclose = models.SmallIntegerField()
    slideshow = models.SmallIntegerField()
    width = models.TextField() # This field type is a guess.
    height = models.TextField() # This field type is a guess.
    bgcolor = models.CharField(max_length=7)
    displayleft = models.SmallIntegerField()
    displayleftif = models.SmallIntegerField()
    progressbar = models.SmallIntegerField()
    highscores = models.SmallIntegerField()
    maxhighscores = models.TextField() # This field type is a guess.
    available = models.TextField() # This field type is a guess.
    deadline = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lesson'

class MdlLessonPages(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    prevpageid = models.TextField() # This field type is a guess.
    nextpageid = models.TextField() # This field type is a guess.
    qtype = models.SmallIntegerField()
    qoption = models.SmallIntegerField()
    layout = models.SmallIntegerField()
    display = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    title = models.CharField(max_length=255)
    contents = models.TextField()
    class Meta:
        db_table = u'mdl_lesson_pages'

class MdlLessonAnswers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    pageid = models.TextField() # This field type is a guess.
    jumpto = models.TextField() # This field type is a guess.
    grade = models.SmallIntegerField()
    score = models.TextField() # This field type is a guess.
    flags = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    answer = models.TextField()
    response = models.TextField()
    class Meta:
        db_table = u'mdl_lesson_answers'

class MdlLessonAttempts(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    pageid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    answerid = models.TextField() # This field type is a guess.
    retry = models.SmallIntegerField()
    correct = models.TextField() # This field type is a guess.
    useranswer = models.TextField()
    timeseen = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lesson_attempts'

class MdlLessonGrades(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    grade = models.FloatField()
    late = models.SmallIntegerField()
    completed = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lesson_grades'

class MdlLessonDefault(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    practice = models.SmallIntegerField()
    modattempts = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    conditions = models.TextField()
    grade = models.SmallIntegerField()
    custom = models.SmallIntegerField()
    ongoing = models.SmallIntegerField()
    usemaxgrade = models.SmallIntegerField()
    maxanswers = models.SmallIntegerField()
    maxattempts = models.SmallIntegerField()
    review = models.SmallIntegerField()
    nextpagedefault = models.SmallIntegerField()
    feedback = models.SmallIntegerField()
    minquestions = models.SmallIntegerField()
    maxpages = models.SmallIntegerField()
    timed = models.SmallIntegerField()
    maxtime = models.TextField() # This field type is a guess.
    retake = models.SmallIntegerField()
    mediaheight = models.TextField() # This field type is a guess.
    mediawidth = models.TextField() # This field type is a guess.
    mediaclose = models.SmallIntegerField()
    slideshow = models.SmallIntegerField()
    width = models.TextField() # This field type is a guess.
    height = models.TextField() # This field type is a guess.
    bgcolor = models.CharField(max_length=7)
    displayleft = models.SmallIntegerField()
    displayleftif = models.SmallIntegerField()
    progressbar = models.SmallIntegerField()
    highscores = models.SmallIntegerField()
    maxhighscores = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lesson_default'

class MdlLessonTimer(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    starttime = models.TextField() # This field type is a guess.
    lessontime = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lesson_timer'

class MdlLessonBranch(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    pageid = models.TextField() # This field type is a guess.
    retry = models.TextField() # This field type is a guess.
    flag = models.SmallIntegerField()
    timeseen = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_lesson_branch'

class MdlLessonHighScores(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    lessonid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    gradeid = models.TextField() # This field type is a guess.
    nickname = models.CharField(max_length=5)
    class Meta:
        db_table = u'mdl_lesson_high_scores'

class MdlQuestionCategories(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=255)
    contextid = models.TextField() # This field type is a guess.
    info = models.TextField()
    stamp = models.CharField(max_length=255)
    parent = models.TextField() # This field type is a guess.
    sortorder = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question_categories'

class MdlQuestion(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    category = models.TextField() # This field type is a guess.
    parent = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    questiontext = models.TextField()
    questiontextformat = models.SmallIntegerField()
    image = models.CharField(max_length=255)
    generalfeedback = models.TextField()
    defaultgrade = models.TextField() # This field type is a guess.
    penalty = models.FloatField()
    qtype = models.CharField(max_length=20)
    length = models.TextField() # This field type is a guess.
    stamp = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    hidden = models.SmallIntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    createdby = models.TextField() # This field type is a guess.
    modifiedby = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question'

class MdlQuestionAnswers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    answer = models.TextField()
    fraction = models.FloatField()
    feedback = models.TextField()
    class Meta:
        db_table = u'mdl_question_answers'

class MdlQuestionDatasetDefinitions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    category = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    type = models.TextField() # This field type is a guess.
    options = models.CharField(max_length=255)
    itemcount = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question_dataset_definitions'

class MdlQuestionDatasetItems(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    definition = models.TextField() # This field type is a guess.
    itemnumber = models.TextField() # This field type is a guess.
    value = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_question_dataset_items'

class MdlQuestionDatasets(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    datasetdefinition = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question_datasets'

class MdlQuestionNumericalUnits(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    multiplier = models.DecimalField(max_digits=40, decimal_places=20)
    unit = models.CharField(max_length=50)
    class Meta:
        db_table = u'mdl_question_numerical_units'

class MdlQuestionAttempts(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    modulename = models.CharField(max_length=20)
    class Meta:
        db_table = u'mdl_question_attempts'

class MdlQuestionStates(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    attempt = models.TextField() # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    originalquestion = models.TextField() # This field type is a guess.
    seq_number = models.IntegerField()
    answer = models.TextField()
    timestamp = models.TextField() # This field type is a guess.
    event = models.SmallIntegerField()
    grade = models.FloatField()
    raw_grade = models.FloatField()
    penalty = models.FloatField()
    class Meta:
        db_table = u'mdl_question_states'

class MdlQuestionSessions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    attemptid = models.TextField() # This field type is a guess.
    questionid = models.TextField() # This field type is a guess.
    newest = models.TextField() # This field type is a guess.
    newgraded = models.TextField() # This field type is a guess.
    sumpenalty = models.FloatField()
    manualcomment = models.TextField()
    class Meta:
        db_table = u'mdl_question_sessions'

class MdlQuiz(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    intro = models.TextField()
    timeopen = models.TextField() # This field type is a guess.
    timeclose = models.TextField() # This field type is a guess.
    optionflags = models.TextField() # This field type is a guess.
    penaltyscheme = models.SmallIntegerField()
    attempts = models.IntegerField()
    attemptonlast = models.SmallIntegerField()
    grademethod = models.SmallIntegerField()
    decimalpoints = models.SmallIntegerField()
    review = models.TextField() # This field type is a guess.
    questionsperpage = models.TextField() # This field type is a guess.
    shufflequestions = models.SmallIntegerField()
    shuffleanswers = models.SmallIntegerField()
    questions = models.TextField()
    sumgrades = models.TextField() # This field type is a guess.
    grade = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    timelimit = models.TextField() # This field type is a guess.
    password = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)
    popup = models.SmallIntegerField()
    delay1 = models.TextField() # This field type is a guess.
    delay2 = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_quiz'

class MdlQuizAttempts(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    uniqueid = models.TextField(unique=True) # This field type is a guess.
    quiz = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    attempt = models.IntegerField()
    sumgrades = models.FloatField()
    timestart = models.TextField() # This field type is a guess.
    timefinish = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    layout = models.TextField()
    preview = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_quiz_attempts'

class MdlQuizGrades(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    quiz = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    grade = models.FloatField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_quiz_grades'

class MdlQuizQuestionInstances(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    quiz = models.TextField() # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    grade = models.IntegerField()
    class Meta:
        db_table = u'mdl_quiz_question_instances'

class MdlQuizQuestionVersions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    quiz = models.TextField() # This field type is a guess.
    oldquestion = models.TextField() # This field type is a guess.
    newquestion = models.TextField() # This field type is a guess.
    originalquestion = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    timestamp = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_quiz_question_versions'

class MdlQuizFeedback(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    quizid = models.TextField() # This field type is a guess.
    feedbacktext = models.TextField()
    mingrade = models.FloatField()
    maxgrade = models.FloatField()
    class Meta:
        db_table = u'mdl_quiz_feedback'

class MdlResource(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    reference = models.CharField(max_length=255)
    summary = models.TextField()
    alltext = models.TextField()
    popup = models.TextField()
    options = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_resource'

class MdlScorm(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    summary = models.TextField()
    version = models.CharField(max_length=9)
    maxgrade = models.FloatField()
    grademethod = models.SmallIntegerField()
    whatgrade = models.TextField() # This field type is a guess.
    maxattempt = models.TextField() # This field type is a guess.
    updatefreq = models.SmallIntegerField()
    md5hash = models.CharField(max_length=32)
    launch = models.TextField() # This field type is a guess.
    skipview = models.SmallIntegerField()
    hidebrowse = models.SmallIntegerField()
    hidetoc = models.SmallIntegerField()
    hidenav = models.SmallIntegerField()
    auto = models.SmallIntegerField()
    popup = models.SmallIntegerField()
    options = models.CharField(max_length=255)
    width = models.TextField() # This field type is a guess.
    height = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_scorm'

class MdlScormScoes(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scorm = models.TextField() # This field type is a guess.
    manifest = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    parent = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    launch = models.CharField(max_length=255)
    scormtype = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_scorm_scoes'

class MdlScormScoesData(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    value = models.TextField()
    class Meta:
        db_table = u'mdl_scorm_scoes_data'

class MdlScormScoesTrack(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    scormid = models.TextField() # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    attempt = models.TextField() # This field type is a guess.
    element = models.CharField(max_length=255)
    value = models.TextField()
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_scorm_scoes_track'

class MdlScormSeqObjective(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    primaryobj = models.SmallIntegerField()
    objectiveid = models.TextField() # This field type is a guess.
    satisfiedbymeasure = models.SmallIntegerField()
    minnormalizedmeasure = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_scorm_seq_objective'

class MdlScormSeqMapinfo(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    objectiveid = models.TextField() # This field type is a guess.
    targetobjectiveid = models.TextField() # This field type is a guess.
    readsatisfiedstatus = models.SmallIntegerField()
    readnormalizedmeasure = models.SmallIntegerField()
    writesatisfiedstatus = models.SmallIntegerField()
    writenormalizedmeasure = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_scorm_seq_mapinfo'

class MdlScormSeqRuleconds(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    conditioncombination = models.CharField(max_length=3)
    ruletype = models.SmallIntegerField()
    action = models.CharField(max_length=25)
    class Meta:
        db_table = u'mdl_scorm_seq_ruleconds'

class MdlScormSeqRulecond(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    ruleconditionsid = models.TextField() # This field type is a guess.
    refrencedobjective = models.CharField(max_length=255)
    measurethreshold = models.TextField() # This field type is a guess.
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=30)
    class Meta:
        db_table = u'mdl_scorm_seq_rulecond'

class MdlScormSeqRolluprule(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    childactivityset = models.CharField(max_length=15)
    minimumcount = models.TextField() # This field type is a guess.
    minimumpercent = models.TextField() # This field type is a guess.
    conditioncombination = models.CharField(max_length=3)
    action = models.CharField(max_length=15)
    class Meta:
        db_table = u'mdl_scorm_seq_rolluprule'

class MdlScormSeqRolluprulecond(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    scoid = models.TextField() # This field type is a guess.
    rollupruleid = models.TextField() # This field type is a guess.
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=25)
    class Meta:
        db_table = u'mdl_scorm_seq_rolluprulecond'

class MdlSurvey(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    template = models.TextField() # This field type is a guess.
    days = models.IntegerField()
    timecreated = models.TextField() # This field type is a guess.
    timemodified = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    intro = models.TextField()
    questions = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_survey'

class MdlSurveyQuestions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    text = models.CharField(max_length=255)
    shorttext = models.CharField(max_length=30)
    multi = models.CharField(max_length=100)
    intro = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    options = models.TextField()
    class Meta:
        db_table = u'mdl_survey_questions'

class MdlSurveyAnswers(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    survey = models.TextField() # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    time = models.TextField() # This field type is a guess.
    answer1 = models.TextField()
    answer2 = models.TextField()
    class Meta:
        db_table = u'mdl_survey_answers'

class MdlSurveyAnalysis(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    survey = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    notes = models.TextField()
    class Meta:
        db_table = u'mdl_survey_analysis'

class MdlWiki(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    summary = models.TextField()
    pagename = models.CharField(max_length=255)
    wtype = models.CharField(max_length=20)
    ewikiprinttitle = models.SmallIntegerField()
    htmlmode = models.SmallIntegerField()
    ewikiacceptbinary = models.SmallIntegerField()
    disablecamelcase = models.SmallIntegerField()
    setpageflags = models.SmallIntegerField()
    strippages = models.SmallIntegerField()
    removepages = models.SmallIntegerField()
    revertchanges = models.SmallIntegerField()
    initialcontent = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_wiki'

class MdlWikiEntries(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    wikiid = models.TextField() # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    pagename = models.CharField(max_length=255)
    timemodified = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_wiki_entries'

class MdlWikiPages(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    pagename = models.CharField(max_length=160)
    version = models.TextField() # This field type is a guess.
    flags = models.TextField() # This field type is a guess.
    content = models.TextField()
    author = models.CharField(max_length=100)
    userid = models.TextField() # This field type is a guess.
    created = models.TextField() # This field type is a guess.
    lastmodified = models.TextField() # This field type is a guess.
    refs = models.TextField()
    meta = models.TextField()
    hits = models.TextField() # This field type is a guess.
    wiki = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_wiki_pages'

class MdlWikiLocks(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    wikiid = models.TextField() # This field type is a guess.
    pagename = models.CharField(max_length=160)
    lockedby = models.TextField() # This field type is a guess.
    lockedsince = models.TextField() # This field type is a guess.
    lockedseen = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_wiki_locks'

class MdlWorkshop(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    course = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    description = models.TextField()
    wtype = models.SmallIntegerField()
    nelements = models.SmallIntegerField()
    nattachments = models.SmallIntegerField()
    phase = models.SmallIntegerField()
    format = models.SmallIntegerField()
    gradingstrategy = models.SmallIntegerField()
    resubmit = models.SmallIntegerField()
    agreeassessments = models.SmallIntegerField()
    hidegrades = models.SmallIntegerField()
    anonymous = models.SmallIntegerField()
    includeself = models.SmallIntegerField()
    maxbytes = models.TextField() # This field type is a guess.
    submissionstart = models.TextField() # This field type is a guess.
    assessmentstart = models.TextField() # This field type is a guess.
    submissionend = models.TextField() # This field type is a guess.
    assessmentend = models.TextField() # This field type is a guess.
    releasegrades = models.TextField() # This field type is a guess.
    grade = models.SmallIntegerField()
    gradinggrade = models.SmallIntegerField()
    ntassessments = models.SmallIntegerField()
    assessmentcomps = models.SmallIntegerField()
    nsassessments = models.SmallIntegerField()
    overallocation = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    teacherweight = models.SmallIntegerField()
    showleaguetable = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    class Meta:
        db_table = u'mdl_workshop'

class MdlWorkshopElements(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    elementno = models.SmallIntegerField()
    description = models.TextField()
    scale = models.SmallIntegerField()
    maxscore = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    stddev = models.FloatField()
    totalassessments = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_workshop_elements'

class MdlWorkshopRubrics(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    elementno = models.TextField() # This field type is a guess.
    rubricno = models.SmallIntegerField()
    description = models.TextField()
    class Meta:
        db_table = u'mdl_workshop_rubrics'

class MdlWorkshopSubmissions(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    title = models.CharField(max_length=100)
    timecreated = models.TextField() # This field type is a guess.
    mailed = models.SmallIntegerField()
    description = models.TextField()
    gradinggrade = models.SmallIntegerField()
    finalgrade = models.SmallIntegerField()
    late = models.SmallIntegerField()
    nassessments = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_workshop_submissions'

class MdlWorkshopAssessments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    submissionid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    timegraded = models.TextField() # This field type is a guess.
    timeagreed = models.TextField() # This field type is a guess.
    grade = models.FloatField()
    gradinggrade = models.SmallIntegerField()
    teachergraded = models.SmallIntegerField()
    mailed = models.SmallIntegerField()
    resubmission = models.SmallIntegerField()
    donotuse = models.SmallIntegerField()
    generalcomment = models.TextField()
    teachercomment = models.TextField()
    class Meta:
        db_table = u'mdl_workshop_assessments'

class MdlWorkshopGrades(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    assessmentid = models.TextField() # This field type is a guess.
    elementno = models.TextField() # This field type is a guess.
    feedback = models.TextField()
    grade = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_workshop_grades'

class MdlWorkshopStockcomments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    elementno = models.TextField() # This field type is a guess.
    comments = models.TextField()
    class Meta:
        db_table = u'mdl_workshop_stockcomments'

class MdlWorkshopComments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    workshopid = models.TextField() # This field type is a guess.
    assessmentid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    mailed = models.SmallIntegerField()
    comments = models.TextField()
    class Meta:
        db_table = u'mdl_workshop_comments'

class MdlQuestionCalculated(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    answer = models.TextField() # This field type is a guess.
    tolerance = models.CharField(max_length=20)
    tolerancetype = models.TextField() # This field type is a guess.
    correctanswerlength = models.TextField() # This field type is a guess.
    correctanswerformat = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question_calculated'

class MdlQuestionMatch(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    subquestions = models.CharField(max_length=255)
    shuffleanswers = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_question_match'

class MdlQuestionMatchSub(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    code = models.TextField() # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    questiontext = models.TextField()
    answertext = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_question_match_sub'

class MdlQuestionMultianswer(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    sequence = models.TextField()
    class Meta:
        db_table = u'mdl_question_multianswer'

class MdlQuestionMultichoice(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    layout = models.SmallIntegerField()
    answers = models.CharField(max_length=255)
    single = models.SmallIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    partiallycorrectfeedback = models.TextField()
    incorrectfeedback = models.TextField()
    answernumbering = models.CharField(max_length=10)
    class Meta:
        db_table = u'mdl_question_multichoice'

class MdlQuestionNumerical(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    answer = models.TextField() # This field type is a guess.
    tolerance = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_question_numerical'

class MdlQuestionRandomsamatch(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    choose = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question_randomsamatch'

class MdlQuestionShortanswer(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    answers = models.CharField(max_length=255)
    usecase = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_question_shortanswer'

class MdlQuestionTruefalse(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    question = models.TextField() # This field type is a guess.
    trueanswer = models.TextField() # This field type is a guess.
    falseanswer = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_question_truefalse'

class MdlBackupFiles(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    backup_code = models.TextField() # This field type is a guess.
    file_type = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    old_id = models.TextField() # This field type is a guess.
    new_id = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_backup_files'

class MdlBackupIds(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    backup_code = models.TextField() # This field type is a guess.
    table_name = models.CharField(max_length=30)
    old_id = models.TextField() # This field type is a guess.
    new_id = models.TextField() # This field type is a guess.
    info = models.TextField()
    class Meta:
        db_table = u'mdl_backup_ids'

class MdlBackupConfig(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_backup_config'

class MdlBackupCourses(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField(unique=True) # This field type is a guess.
    laststarttime = models.TextField() # This field type is a guess.
    lastendtime = models.TextField() # This field type is a guess.
    laststatus = models.CharField(max_length=1)
    nextstarttime = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_backup_courses'

class MdlBackupLog(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    time = models.TextField() # This field type is a guess.
    laststarttime = models.TextField() # This field type is a guess.
    info = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_backup_log'

class MdlBlock(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    name = models.CharField(max_length=40)
    version = models.TextField() # This field type is a guess.
    cron = models.TextField() # This field type is a guess.
    lastcron = models.TextField() # This field type is a guess.
    visible = models.SmallIntegerField()
    multiple = models.SmallIntegerField()
    class Meta:
        db_table = u'mdl_block'

class MdlBlockInstance(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    blockid = models.TextField() # This field type is a guess.
    pageid = models.TextField() # This field type is a guess.
    pagetype = models.CharField(max_length=20)
    position = models.CharField(max_length=10)
    weight = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    configdata = models.TextField()
    class Meta:
        db_table = u'mdl_block_instance'

class MdlBlockPinned(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    blockid = models.TextField() # This field type is a guess.
    pagetype = models.CharField(max_length=20)
    position = models.CharField(max_length=10)
    weight = models.SmallIntegerField()
    visible = models.SmallIntegerField()
    configdata = models.TextField()
    class Meta:
        db_table = u'mdl_block_pinned'

class MdlBlockRssClient(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    title = models.TextField()
    preferredtitle = models.CharField(max_length=64)
    description = models.TextField()
    shared = models.SmallIntegerField()
    url = models.CharField(max_length=255)
    class Meta:
        db_table = u'mdl_block_rss_client'

class MdlBlockSearchDocuments(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    docid = models.CharField(max_length=32)
    doctype = models.CharField(max_length=32)
    itemtype = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    docdate = models.TextField() # This field type is a guess.
    updated = models.TextField() # This field type is a guess.
    courseid = models.TextField() # This field type is a guess.
    groupid = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_block_search_documents'

class MdlEnrolAuthorize(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    paymentmethod = models.CharField(max_length=6)
    refundinfo = models.SmallIntegerField()
    ccname = models.CharField(max_length=255)
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    transid = models.TextField() # This field type is a guess.
    status = models.TextField() # This field type is a guess.
    timecreated = models.TextField() # This field type is a guess.
    settletime = models.TextField() # This field type is a guess.
    amount = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    class Meta:
        db_table = u'mdl_enrol_authorize'

class MdlEnrolAuthorizeRefunds(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    orderid = models.TextField() # This field type is a guess.
    status = models.SmallIntegerField()
    amount = models.CharField(max_length=10)
    transid = models.TextField() # This field type is a guess.
    settletime = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_enrol_authorize_refunds'

class MdlEnrolPaypal(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    business = models.CharField(max_length=255)
    receiver_email = models.CharField(max_length=255)
    receiver_id = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    courseid = models.TextField() # This field type is a guess.
    userid = models.TextField() # This field type is a guess.
    memo = models.CharField(max_length=255)
    tax = models.CharField(max_length=255)
    option_name1 = models.CharField(max_length=255)
    option_selection1_x = models.CharField(max_length=255)
    option_name2 = models.CharField(max_length=255)
    option_selection2_x = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    pending_reason = models.CharField(max_length=255)
    reason_code = models.CharField(max_length=30)
    txn_id = models.CharField(max_length=255)
    parent_txn_id = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=30)
    timeupdated = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'mdl_enrol_paypal'

