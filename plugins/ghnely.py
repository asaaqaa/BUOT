##########
#By: @WWWL5 
##########


import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

@Client.on_callback_query(filters.regex("^ghnely (\\d+)$"))
async def ghnely(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("ام كلثوم", callback_data="klthom " + str(m.from_user.id))] +
        [InlineKeyboardButton("رضا البحراوي", callback_data="bhrawy " + str(m.from_user.id))],
        [InlineKeyboardButton("تامر حسني", callback_data="hosny " + str(m.from_user.id))] +
        [InlineKeyboardButton("تامر عاشور", callback_data="ashor " + str(m.from_user.id))],
        [InlineKeyboardButton("عمرو دياب", callback_data="diab " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد حماقي", callback_data="hmaqy " + str(m.from_user.id))],
        [InlineKeyboardButton("محمد منير", callback_data="monir " + str(m.from_user.id))] +
        [InlineKeyboardButton("مسلم", callback_data="muslim " + str(m.from_user.id))],
        [InlineKeyboardButton("راب مصري", callback_data="rap " + str(m.from_user.id))] +
        [InlineKeyboardButton("ويجز", callback_data="wegz " + str(m.from_user.id))],
        [InlineKeyboardButton("عصام صاصا", callback_data="sasa " + str(m.from_user.id))] +
        [InlineKeyboardButton("حسن شاكوش", callback_data="shakosh " + str(m.from_user.id))],
        [InlineKeyboardButton("حمو بيكا", callback_data="beka " + str(m.from_user.id))] +
        [InlineKeyboardButton("حمو الطيخا", callback_data="tekha " + str(m.from_user.id))],
        [InlineKeyboardButton("حوده بندق", callback_data="bondq " + str(m.from_user.id))] +
        [InlineKeyboardButton("سامر المدني", callback_data="madany " + str(m.from_user.id))],
        [InlineKeyboardButton("احمد كامل", callback_data="kamel " + str(m.from_user.id))] +
        [InlineKeyboardButton("عمار حسني", callback_data="ammar " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ عاوزني اغنيلك لمين يازميكس\n√", reply_markup=keyboard)
 
#########################################################################################
#########################################################################################
 
@Client.on_callback_query(filters.regex("^klthom (\\d+)$"))
async def klthom(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255", "256"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^bhrawy (\\d+)$"))
async def bhrawy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^hosny (\\d+)$"))
async def hosny(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^ashor (\\d+)$"))
async def ashor(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^diab (\\d+)$"))
async def diab(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^hmaqy (\\d+)$"))
async def hmaqy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657", "658", "659", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "670", "671", "672", "673", "674", "675", "676", "677", "678", "679", "680", "681", "682", "683", "684", "685", "686", "687", "688", "689", "690", "691", "692", "693", "694", "695", "696", "697", "698", "699", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744", "745", "746", "747", "748", "749", "750", "751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^monir (\\d+)$"))
async def monir(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^muslim (\\d+)$"))
async def muslim(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1064", "1065", "1066", "1067", "1068", "1069", "1070", "1071", "1072", "1073", "1074", "1075", "1076", "1077", "1078", "1079", "814", "816", "817", "825", "848", "853", "885", "884", "883", "886", "887", "888", "889"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^rap (\\d+)$"))
async def rap(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "890", "891", "892", "893", "894", "895", "896", "897", "898", "899", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^wegz (\\d+)$"))
async def wegz(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "935", "936", "937", "938", "939", "940", "941", "942", "943", "944", "945", "946", "947", "948", "949", "950", "951", "952", "953", "954", "955", "956", "957", "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "976", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999", "1000", "1001", "1002", "1003"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^sasa (\\d+)$"))
async def sasa(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1032", "1033", "1034", "1035", "1036", "1037", "1038", "1039", "1040", "1041", "1042", "1043", "1044", "1045", "1046", "1047", "1048", "1049", "1050", "1051", "1052", "1053", "1054", "1055", "1056", "1057", "1058", "1059", "1060", "1061", "1062", "1063"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^shakosh (\\d+)$"))
async def shakosh(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1080", "1081", "1082", "1083", "1084", "1085", "1086", "1087", "1088", "1089", "1090", "1091", "1092", "1093"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^beka (\\d+)$"))
async def beka(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1094", "1095", "1096", "1097", "1098", "1099", "1100", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^tekha (\\d+)$"))
async def tekha(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1131", "1132", "1133", "1134", "1135", "1136", "1137", "1138", "1139", "1140", "1141", "1142", "1143", "1144", "1145", "1146", "1147", "1148", "1149", "1150", "1151", "1152", "1153", "1154", "1155", "1156", "1157", "1158", "1159", "1160", "1161", "1162", "1163", "1164", "1165", "1166", "1167", "1168", "1169", "1170", "1171", "1172", "1173", "1174", "1175", "1176", "1177", "1178", "1179", "1180", "1181", "1182", "1183", "1184", "1185", "1186", "1187", "1188", "1189", "1190", "1191", "1192", "1193", "1194", "1195", "1196", "1197", "1198", "1199", "1200", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "1232", "1233", "1234", "1235", "1236", "1237", "1238", "1239", "1240", "1241", "1242", "1243", "1244", "1245", "1246", "1247", "1248", "1249", "1250", "1251", "1252", "1253", "1254", "1255", "1256", "1257", "1258"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^bondq (\\d+)$"))
async def bondq(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1259", "1260", "1261", "1262", "1263", "1264", "1265", "1266", "1267", "1268", "1269", "1270", "1271", "1272", "1273", "1274", "1275", "1276", "1277", "1278", "1279", "1280", "1281", "1282", "1283", "1284", "1285", "1286", "1287", "1288", "1289", "1290", "1291", "1292", "1293", "1294", "1295", "1296"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^madany (\\d+)$"))
async def madany(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1297", "1298"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^kamel (\\d+)$"))
async def kamel(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1299", "1300", "1301", "1302", "1303", "1304", "1305", "1306", "1307", "1308", "1309", "1310", "1311", "1312", "1313", "1314", "1315", "1316", "1317", "1318", "1319", "1320", "1321", "1322", "1323", "1324", "1325", "1326", "1327", "1328", "1329", "1330", "1331", "1332", "1333", "1334"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^ammar (\\d+)$"))
async def ammar(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    ghnelyaudio = [
                "1335", "1336", "1337", "1338", "1339", "1340", "1341", "1342", "1343", "1344", "1345", "1346", "1347", "1348", "1349", "1350", "1351", "1352", "1353", "1354", "1355", "1356", "1357", "1358", "1359", "1360", "1361", "1362"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_audio("https://t.me/UDFIO/" + random.choice(ghnelyaudio),
                                caption=f"By: @{get_bot_information()[1]}"),
