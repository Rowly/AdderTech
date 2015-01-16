'''
Created on 18 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import unittest
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.services.parameters import parameter_singleton

class AimDashboardSettingsTimePageFunctionsTest(BaseAimRegressionTest):
    
    africas = ["Abidjan", "Accra", "Addis Ababa", "Algiers",
               "Asmara", "Bamako", "Bangui", "Banjul", "Bissau",
               "Blantyre", "Brazzaville", "Bujumbura", "Cairo",
               "Casablanca", "Ceuta", "Conakry", "Dakar", "Dar es Salaam",
               "Djibouti", "Douala", "El Aaiun", "Freetown", "Gaborone", 
               "Harare", "Johannesburg", "Kampala", "Khartoum", "Kigali", 
               "Kinshasa", "Lagos", "Libreville", "Lome", "Luanda", 
               "Lubumbashi", "Lusaka", "Malabo", "Maputo", "Maseru", 
               "Mbabane", "Mogadishu", "Monrovia", "Nairobi", "Ndjamena", 
               "Niamey", "Nouakchott", "Ouagadougou", "Porto-Novo", 
               "Sao Tome", "Tripoli", "Tunis", "Windhoek"]
    americas = ["Adak", "Anchorage", "Anguilla", "Antigua", "Araguaina", 
               "Argentina/Buenos Aires", "Argentina/Catamarca", 
               "Argentina/Cordoba", "Argentina/Jujuy", "Argentina/La Rioja", 
               "Argentina/Mendoza", "Argentina/Rio Gallegos", "Argentina/Salta", 
               "Argentina/San Juan", "Argentina/San Luis", "Argentina/Tucuman", 
               "Argentina/Ushuaia", "Aruba", "Asuncion", "Atikokan", "Bahia", 
               "Bahia Banderas", "Barbados", "Belem", "Belize", "Blanc-Sablon", 
               "Boa Vista", "Bogota", "Boise", "Cambridge Bay", "Campo Grande", 
               "Cancun", "Caracas", "Cayenne", "Cayman", "Chicago", "Chihuahua", 
               "Costa Rica", "Cuiaba", "Curacao", "Danmarkshavn", "Dawson", 
               "Dawson Creek", "Denver", "Detroit", "Dominica", "Edmonton", 
               "Eirunepe", "El Salvador", "Fortaleza", "Glace Bay", "Godthab", 
               "Goose Bay", "Grand Turk", "Grenada", "Guadeloupe", "Guatemala", 
               "Guayaquil", "Guyana", "Halifax", "Havana", "Hermosillo", 
               "Indiana/Indianapolis", "Indiana/Knox", "Indiana/Marengo", 
               "Indiana/Petersburg", "Indiana/Tell City", "Indiana/Vevay", 
               "Indiana/Vincennes", "Indiana/Winamac", "Inuvik", "Iqaluit", 
               "Jamaica", "Juneau", "Kentucky/Louisville", "Kentucky/Monticello", 
               "La Paz", "Lima", "Los Angeles", "Maceio", "Managua", "Manaus", 
               "Marigot", "Martinique", "Matamoros", "Mazatlan", "Menominee", 
               "Merida", "Mexico City", "Miquelon", "Moncton", "Monterrey", 
               "Montevideo", "Montreal", "Montserrat", "Nassau", "New York", 
               "Nipigon", "Nome", "Noronha", "North Dakota/Center", 
               "North Dakota/New Salem", "Ojinaga", "Panama", "Pangnirtung", 
               "Paramaribo", "Phoenix", "Port of Spain", "Port-au-Prince", 
               "Porto Velho", "Puerto Rico", "Rainy River", "Rankin Inlet", 
               "Recife", "Regina", "Resolute", "Rio Branco", "Santa Isabel", 
               "Santarem", "Santiago", "Santo Domingo", "Sao Paulo", 
               "Scoresbysund", "Shiprock", "St Barthelemy", "St Johns", 
               "St Kitts", "St Lucia", "St Thomas", "St Vincent", 
               "Swift Current", "Tegucigalpa", "Thule", "Thunder Bay", 
               "Tijuana", "Toronto", "Tortola", "Vancouver", "Whitehorse", 
               "Winnipeg", "Yakutat", "Yellowknife"]
    antarcticas = ["Casey", "Davis", "DumontDUrville", "Macquarie", "Mawson", 
                  "McMurdo", "Palmer", "Rothera", "South Pole", "Syowa", "Vostok"]
    arctics = ["Longyearbyen"]
    asias = ["Aden", "Almaty", "Amman", "Anadyr", "Aqtau", "Aqtobe", "Ashgabat", 
             "Baghdad", "Bahrain", "Baku", "Bangkok", "Beirut", "Bishkek", 
             "Brunei", "Choibalsan", "Chongqing", "Colombo", "Damascus", "Dhaka", 
             "Dili", "Dubai", "Dushanbe", "Gaza", "Harbin", "Ho Chi Minh", 
             "Hong Kong", "Hovd", "Irkutsk", "Jakarta", "Jayapura", "Jerusalem", 
             "Kabul", "Kamchatka", "Karachi", "Kashgar", "Kathmandu", "Kolkata", 
             "Krasnoyarsk", "Kuala Lumpur", "Kuching", "Kuwait", "Macau", 
             "Magadan", "Makassar", "Manila", "Muscat", "Nicosia", 
             "Novokuznetsk", "Novosibirsk", "Omsk", "Oral", "Phnom Penh", 
             "Pontianak", "Pyongyang", "Qatar", "Qyzylorda", "Rangoon", "Riyadh", 
             "Sakhalin", "Samarkand", "Seoul", "Shanghai", "Singapore", "Taipei", 
             "Tashkent", "Tbilisi", "Tehran", "Thimphu", "Tokyo", "Ulaanbaatar", 
             "Urumqi", "Vientiane", "Vladivostok", "Yakutsk", "Yekaterinburg", 
             "Yerevan"]
    atlantics = ["Azores", "Bermuda", "Canary", "Cape Verde", "Faroe", "Madeira", 
                 "Reykjavik", "South Georgia", "St Helena", "Stanley"]
    australias = ["Adelaide", "Brisbane", "Broken Hill", "Currie", "Darwin", 
                  "Eucla", "Hobart", "Lindeman", "Lord Howe", "Melbourne", "Perth", 
                  "Sydney"]
    europes = ["Amsterdam", "Andorra", "Athens", "Belgrade", "Berlin", 
               "Bratislava", "Brussels", "Bucharest", "Budapest", "Chisinau", 
               "Copenhagen", "Dublin", "Gibraltar", "Guernsey", "Helsinki", 
               "Isle of Man", "Istanbul", "Jersey", "Kaliningrad", "Kiev", 
               "Lisbon", "Ljubljana", "London", "Luxembourg", "Madrid", "Malta", 
               "Mariehamn", "Minsk", "Monaco", "Moscow", "Oslo", "Paris", 
               "Podgorica", "Prague", "Riga", "Rome", "Samara", "San Marino", 
               "Sarajevo", "Simferopol", "Skopje", "Sofia", "Stockholm", 
               "Tallinn", "Tirane", "Uzhgorod", "Vaduz", "Vatican", "Vienna", 
               "Vilnius", "Volgograd", "Warsaw", "Zagreb", "Zaporozhye", "Zurich"]
    indians = ["Antananarivo", "Chagos", "Christmas", "Cocos", "Comoro", 
               "Kerguelen", "Mahe", "Maldives", "Mauritius", "Mayotte", "Reunion"]
    pacifics = ["Apia", "Auckland", "Chatham", "Easter", "Efate", "Enderbury", 
                "Fakaofo", "Fiji", "Funafuti", "Galapagos", "Gambier", 
                "Guadalcanal", "Guam", "Honolulu", "Johnston", "Kiritimati", 
                "Kosrae", "Kwajalein", "Majuro", "Marquesas", "Midway", "Nauru", 
                "Niue", "Norfolk", "Noumea", "Pago Pago", "Palau", "Pitcairn", 
                "Ponape", "Port Moresby", "Rarotonga", "Saipan", "Tahiti", 
                "Tarawa", "Tongatapu", "Truk", "Wake", "Wallis"]
    zones = {"Africa":africas, "America":americas, "Antarctica":antarcticas, 
             "Arctic":arctics, "Asia":asias, "Atlantic":atlantics, 
             "Australia":australias, "Europe":europes, "Indian":indians, 
             "Pacific":pacifics}
    
    invalid_feb = ["29", "30", "31"]
    
    def test_when_time_zone_changed_to_africa_regions_updates_correctly(self):
        region = "Africa"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_america_regions_updates_correctly(self):
        region = "America"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_antarctica_regions_updates_correctly(self):
        region = "Antarctica"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_artic_regions_updates_correctly(self):
        region = "Arctic"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_asia_regions_updates_correctly(self):
        region = "Asia"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_atlantic_regions_updates_correctly(self):
        region = "Atlantic"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_australia_regions_updates_correctly(self):
        region = "Australia"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_europe_regions_updates_correctly(self):
        region = "Europe"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_india_regions_updates_correctly(self):
        region = "Indian"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()

    def test_when_time_zone_changed_to_pacific_regions_updates_correctly(self):
        region = "Pacific"
        region_list = self.get_region_list(region)
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self._page.select_time_zone(region)
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self._page.click_save()
        locations = self._page.get_all_time_zone_locations_texts(region)
        for location in locations:
            self.assertTrue(location in region_list)
        check_list = list(set(region_list) - set(locations))
        self.assertTrue(len(check_list) == 0)
        self.reset_time_zone()
    
    def test_ntp_options_are_displayed_when_enabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) <= 3 and int(split_version[1]) < 2:
            raise unittest.SkipTest("NTP added in v3.2")
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_time_settings_button()
        self.assertFalse(self._page.get_display_state_ntp_servername())
        self._page.set_ntp_enabled("yes")
        self.assertTrue(self._page.get_display_state_ntp_servername())
        self._page.set_ntp_enabled("no")
    
    def get_region_list(self, region):
        return self.zones[region]
    
    def reset_date(self, day, month, year):
        self._page.select_time_day(day)
        self._page.select_time_month(month)
        self._page.select_time_year(year)
        self._page.click_save()
    
    def reset_time_zone(self):
        self._page.select_time_zone("Europe")
        self._page.select_time_zone_location("Europe", "London")
        self._page.click_save()
        