from ..constants import parse_encode


class EventResults:
    def __init__(self, dict):
        self.lap_best = parse_encode(dict['38'])
        self.qlap_best = parse_encode(dict['6'])
        self.car_class_id = dict['29']
        self.car_id = dict['32']
        self.category_id = dict['33']
        self.champ_points = dict['40']
        self.champ_points_sort = dict['43']
        self.club_points = dict['16']
        self.club_points_sort = dict['47']
        self.cust_id = dict['23']
        self.display_name = parse_encode(dict['48'])
        self.drop_race_points = dict['17']
        self.event_type = dict['37']
        self.time_finished = dict['10']
        self.pos_finish = dict['3']
        self.group_name = dict['19']
        self.helm_color_1 = dict['1']
        self.helm_color_2 = parse_encode(dict['14'])
        self.helm_color_3 = parse_encode(dict['13'])
        self.helm_license_level = dict['24']
        self.helm_pattern = dict['46']
        self.incidents = dict['39']
        self.license_group = dict['35']
        self.official_session = dict['18']
        self.race_week = dict['8']
        self.time_start_raw = dict['11']
        self.row_number = dict['26']
        self.quarter_season = dict['34']
        self.year = dict['42']
        self.season_id = dict['22']
        self.series_id = dict['20']
        self.rank_session = dict['28']
        self.session_id = dict['9']
        self.date_start = parse_encode(dict['44'])
        self.time_start = parse_encode(dict['21'])
        self.pos_start = dict['12']
        self.strength_of_field = dict['45']
        self.blap_subsession_best = parse_encode(dict['7'])
        self.subsession_id = dict['41']
        self.track_id = dict['30']
        self.winner_display_name = parse_encode(dict['31'])
        self.winner_helm_color_1 = parse_encode(dict['5'])
        self.winner_helm_color_2 = dict['2']
        self.winner_helm_color_3 = parse_encode(dict['4'])
        self.winner_helm_pattern = dict['36']
        self.winner_license_level = dict['25']
        self.winners_group_id = dict['27']
        # Another instance of not in dict
        # self.rowcount = dict['15']


class SeasonStandings:
    def __init__(self, dict):
        self.finish_pos_avg = dict['9']
        self.start_pos_avg = dict['8']
        self.club_id = dict['6']
        self.club_name = parse_encode(dict['23'])
        self.country = parse_encode(dict['1'])
        self.country_code = parse_encode(dict['4'])
        self.cust_id = dict['28']
        self.country_name = dict['32']
        self.display_name = parse_encode(dict['26'])
        self.division = dict['11']
        self.dropped = dict['5']
        self.helm_color_1 = parse_encode(dict['25'])
        self.helm_color_2 = parse_encode(dict['27'])
        self.helm_color_3 = parse_encode(dict['22'])
        self.helm_pattern = dict['20']
        self.incidents = dict['13']
        self.irating = dict['3']
        self.laps = dict['7']
        self.laps_led = dict['24']
        self.max_license_level = dict['21']
        self.points = dict['10']
        self.poles = dict['19']
        self.pos = dict['30']
        self.rank = dict['14']
        self.row = dict['31']
        self.starts = dict['15']
        self.sub_level = parse_encode(dict['29'])
        self.top_five = dict['12']
        self.week = dict['2']
        self.wins = dict['17']

        # Used only on webpage to highlight the member in relaton to others
        # self.custrow = dict['16']
        # self.rowcount = dict['18']


class DriverStats:
    def __init__(self, dict):
        self.field_size_avg = dict['13']
        self.finish_pos_avg = dict['9']
        self.start_pos_avg = dict['8']
        self.incidents_avg = dict['26']
        self.points_avg = dict['27']
        self.club_id = dict['5']
        self.club_name = parse_encode(dict['29'])
        self.club_points = dict['21']
        self.country_code = parse_encode(dict['4'])
        self.cust_id = dict['34']
        self.display_name = parse_encode(dict['32'])
        self.group_letter = parse_encode(dict['39'])
        self.group_name = parse_encode(dict['24'])
        self.helm_color_1 = parse_encode(dict['31'])
        self.helm_color_2 = parse_encode(dict['33'])
        self.helm_color_3 = parse_encode(dict['28'])
        self.helm_face_type = dict['36']
        self.helm_helmet_type = dict['10']
        self.helm_pattern = dict['22']
        self.irating = dict['3']
        self.irating_rank = dict['2']
        self.laps = dict['7']
        self.laps_led = dict['30']
        self.license_class = parse_encode(dict['16'])
        self.license_class_rank = dict['19']
        self.license_class_id = dict['12']
        self.license_level = dict['23']
        self.points = dict['11']
        self.rank = dict['14']
        self.region = parse_encode(dict['38'])
        self.row = dict['37']
        self.starts = dict['15']
        self.sub_level = dict['35']
        self.top_25_percent = dict['1']
        self.ttrating = dict['25']
        self.ttrating_rank = dict['6']
        self.wins = dict['18']
        # These are only used in front end webpage; Not in dict results
        # self.custrow = dict['17']
        # self.rowcount = dict['20']


class WorldRecords:
    def __init__(self, dict):
        self.car_id = dict['9']
        self.category = parse_encode(dict['35'])
        self.cat_id = dict['10']
        self.club_id = dict['7']
        self.club_name = parse_encode(dict['27'])
        self.country_code = parse_encode(dict['6'])
        self.cust_id = dict['31']
        self.display_name = parse_encode(dict['29'])
        self.helm_color_1 = parse_encode(dict['28'])
        self.helm_color_2 = parse_encode(dict['30'])
        self.helm_color_3 = parse_encode(dict['26'])
        self.helm_pattern = dict['22']
        self.irating = dict['4']
        self.license_class = parse_encode(dict['3'])
        self.license_class_id = dict['14']
        self.license_level = dict['23']
        self.practice = parse_encode(dict['2'])
        self.practice_start_time = dict['8']
        self.practice_subsession_id = dict['13']
        self.qualify = parse_encode(dict['15'])
        self.time_start_qualify = dict['21']
        self.qualify_subsession_id = ['36']
        self.race = parse_encode(dict['19'])
        self.race_start_time = dict['18']
        self.race_subsession_id = ['11']
        self.region = parse_encode(dict['34'])
        self.row = dict['33']
        self.season_quarter = parse_encode(dict['12'])
        self.season_year = parse_encode(dict['17'])
        self.sub_level = dict['32']
        self.timetrial = parse_encode(dict['37'])
        self.tt_start_time = dict['25']
        self.tt_subsession_id = ['1']
        self.track_id = dict['5']
        self.ttrating = dict['24']
        # Data not used in the 'r' dictionary. Only for webpage display.
        # self.custrow = dict['16']
        # self.rowcount = dict['20']


class PrivateResults:
    def __init__(self, dict):
        self.lap_best = dict['bestlaptime']
        self.car_class_id = dict['carclassid']
        self.car_ids = dict['carids']
        self.cat_id = dict['catid']
        self.pos_finish_class = dict['classfinishingposition']
        self.pos_start_class = dict['classstartingposition']
        self.created = dict['created']
        self.pos_finish = dict['finishingposition']
        self.fixed_setup = dict['fixed_setup']
        self.full_course_cautions = dict['fullcoursecautions']
        self.hardcore_level = dict['hardcorelevel']
        self.host_cust_id = dict['host_custid']
        self.host_display_name = dict['host_displayname']
        self.host_helmet_color_1 = dict['host_helmet_color1']
        self.host_helmet_color_2 = dict['host_helmet_color2']
        self.host_helmet_color_3 = dict['host_helmet_color3']
        self.host_helmet_face_type = dict['host_helmet_facetype']
        self.host_helmet_helmet_type = dict['host_helmet_helmettype']
        self.host_helmet_pattern = dict['host_helmet_pattern']
        self.host_license_level = dict['host_licenselevel']
        self.incidents = dict['incidents']
        self.lonequalify = dict['lonequalify']
        self.pct_fuel_fills_max = dict['max_pct_fuel_fills']
        self.drivers_max = dict['maxdrivers']
        self.ir_max = dict['maxir']
        self.lic_level_max = dict['maxliclevel']
        self.ir_min = dict['minir']
        self.lic_level_min = dict['minliclevel']
        self.multiclass = dict['multiclass']
        self.fast_tows_num = dict['numfasttows']
        self.practice_length = dict['practicelength']
        self.private = dict['private']
        self.session_id_private = dict['privatesessionid']
        self.laps_qualify = dict['qualifylaps']
        self.length_qualify = dict['qualifylength']
        self.setup_filenames_qual = dict['qualsetupfilenames']
        self.setup_ids_qual = dict['qualsetupids']
        self.race_time_finished = dict['racefinishedat']
        self.laps_race = dict['racelaps']
        self.length_race = dict['racelength']
        self.setup_filenames_race = dict['racesetupfilenames']
        self.setup_ids_race = dict['racesetupids']
        self.restarts = dict['restarts']
        self.row = dict['rn']
        self.rolling_starts = dict['rollingstarts']
        self.session_fast_lap = dict['sessionfastlap']
        self.session_id = dict['sessionid']
        self.session_name = dict['sessionname']
        self.time_start = dict['start_time']
        self.pos_start = dict['startingposition']
        self.subsession_time_finished = dict['subsessionfinishedat']
        self.subsession_id = dict['subsessionid']
        self.time_of_day = dict['timeofday']
        self.track = dict['track_name']
        self.track_id = dict['trackid']
        self.fog_density = dict['weather_fog_density']
        self.humidity = dict['weather_rh']
        self.skies = dict['weather_skies']
        self.temp_unit = dict['weather_temp_units']
        self.temp_value = dict['weather_temp_value']
        self.weather = dict['weather_type']
        self.wind_direction = dict['weather_wind_dir']
        self.wind_speed_unit = dict['weather_wind_speed_units']
        self.wind_speed_value = dict['weather_wind_speed_value']
        self.weight_penalties = dict['weight_penalties']
        self.winner_display_name = dict['winner_displayname']
        self.winner_display_names = dict['winner_displaynames']
        self.winner_helmet_color_1 = dict['winner_helmet_color1']
        self.winner_helmet_color_2 = dict['winner_helmet_color2']
        self.winner_helmet_color_3 = dict['winner_helmet_color3']
        self.winner_helmet_pattern = dict['winner_helmet_pattern']
        self.winner_license_level = dict['winner_licenselevel']
        self.winner_group_id = dict['winnersgroupid']


class SeriesRaceResults:
    def __init__(self, dict):
        self.car_class_id = dict['2']
        self.official = dict['6']
        self.session_id = dict['4']
        self.size_of_field = dict['7']
        self.time_start = dict['1']
        self.strength_of_field = dict['8']
        self.subsession_id = dict['5']
        self.track_id = dict['3']


class Team:
    def __init__(self, dict):
        self.finish_pos_class_avg = dict['avgclassfinishingposition']
        self.size_of_field_class_avg = dict['avgclasssizeoffield']
        self.start_pos_class_avg = dict['avgclassstartingposition']
        self.strength_of_field_class_avg = dict['avgclassstrengthoffield']
        self.finish_pos_event_avg = dict['avgeventfinishingposition']
        self.size_of_field_event_avg = dict['avgeventsizeoffield']
        self.start_pos_event_avg = dict['avgeventstartingposition']
        self.strength_of_field_event_avg = dict['avgeventstrengthoffield']
        self.cars = dict['cars']
        self.poles_class = dict['classpoles']
        self.top_10_pcnt_class = dict['classtop10pcnt']
        self.top_25_percent_class = dict['classtop25pcnt']
        self.top_five_class = dict['classtopfive']
        self.wins_class = dict['classwins']
        self.color_1 = dict['color1']
        self.color_2 = dict['color2']
        self.color_3 = dict['color3']
        self.cust_id = dict['custid']
        self.poles_event = dict['eventpoles']
        self.top_10_pcnt_event = dict['eventtop10pcnt']
        self.top_25_pcnt_event = dict['eventtop25pcnt']
        self.top_five_event = dict['eventtopfive']
        self.wins_event = dict['eventwins']
        self.face_type = dict['facetype']
        self.helmet_type = dict['helmettype']
        self.incidents = dict['incidents']
        self.laps_comp = dict['lapscomplete']
        self.laps_led = dict['lapslead']
        self.license_level = dict['licenselevel']
        self.name = dict['name']
        self.pattern = dict['pattern']
        self.team_ranking = dict['team_ranking']
        self.team_id = dict['teamid']
        self.week_dropped = dict['weekdropped']
        self.week_points = dict['weekpoints']
        self.week_starts = dict['weekstarts']
