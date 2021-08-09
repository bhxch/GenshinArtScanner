Formats = {
    "FIGHT_PROP_CRITICAL": "{:.1%}",
    "FIGHT_PROP_CRITICAL_HURT": "{:.1%}",
    "FIGHT_PROP_ATTACK": "{:,.0f}",
    "FIGHT_PROP_ATTACK_PERCENT": "{:.1%}",
    "FIGHT_PROP_ELEMENT_MASTERY": "{:,.0f}",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "{:.1%}",
    "FIGHT_PROP_HP": "{:,.0f}",
    "FIGHT_PROP_HP_PERCENT": "{:.1%}",
    "FIGHT_PROP_DEFENSE": "{:,.0f}",
    "FIGHT_PROP_DEFENSE_PERCENT": "{:.1%}",
    "FIGHT_PROP_PHYSICAL_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_HEAL_ADD": "{:.1%}",
    "FIGHT_PROP_ROCK_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_WIND_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_ICE_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_WATER_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_FIRE_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_ELEC_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_GRASS_ADD_HURT": "{:.1%}",
    "FIGHT_PROP_FIRE_SUB_HURT": "{:.1%}",
}

MainAttrNames = {
    "FIGHT_PROP_CRITICAL": "暴击率",
    "FIGHT_PROP_CRITICAL_HURT": "暴击伤害",
    "FIGHT_PROP_ATTACK": "攻击力",
    "FIGHT_PROP_ATTACK_PERCENT": "攻击力",
    "FIGHT_PROP_ELEMENT_MASTERY": "元素精通",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "元素充能效率",
    "FIGHT_PROP_HP": "生命值",
    "FIGHT_PROP_HP_PERCENT": "生命值",
    "FIGHT_PROP_DEFENSE": "防御力",
    "FIGHT_PROP_DEFENSE_PERCENT": "防御力",
    "FIGHT_PROP_PHYSICAL_ADD_HURT": "物理伤害加成",
    "FIGHT_PROP_HEAL_ADD": "治疗加成",
    "FIGHT_PROP_ROCK_ADD_HURT": "岩元素伤害加成",
    "FIGHT_PROP_WIND_ADD_HURT": "风元素伤害加成",
    "FIGHT_PROP_ICE_ADD_HURT": "冰元素伤害加成",
    "FIGHT_PROP_WATER_ADD_HURT": "水元素伤害加成",
    "FIGHT_PROP_FIRE_ADD_HURT": "火元素伤害加成",
    "FIGHT_PROP_ELEC_ADD_HURT": "雷元素伤害加成",
    "FIGHT_PROP_GRASS_ADD_HURT": "草元素伤害加成",
    "FIGHT_PROP_FIRE_SUB_HURT": "火元素伤害减免",
}
AttrName2Ids = {v: i.replace('_PERCENT', '') for i, v in MainAttrNames.items()}

TypeNames = ["生之花", "死之羽", "时之沙", "空之杯", "理之冠"]

SubAttrNames = {
    "FIGHT_PROP_CRITICAL": "暴击率",
    "FIGHT_PROP_CRITICAL_HURT": "暴击伤害",
    "FIGHT_PROP_ATTACK": "攻击力",
    "FIGHT_PROP_ATTACK_PERCENT": "攻击力",
    "FIGHT_PROP_ELEMENT_MASTERY": "元素精通",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "元素充能效率",
    "FIGHT_PROP_HP": "生命值",
    "FIGHT_PROP_HP_PERCENT": "生命值",
    "FIGHT_PROP_DEFENSE": "防御力",
    "FIGHT_PROP_DEFENSE_PERCENT": "防御力",
}

RarityToMaxLvs = [4, 4, 12, 16, 20]
RarityToBaseStatNumber = {1:[0], 2:[0,1], 3:[1,2], 4:[2,3], 5:[3,4]}

ArtNames = [
    ["磐陀裂生之花", "嵯峨群峰之翼", "星罗圭璧之晷", "巉岩琢塑之樽", "不动玄石之相"],
    ["历经风雪的思念", "摧冰而行的执望", "冰雪故园的终期", "遍结寒霜的傲骨", "破冰踏雪的回音"],
    ["染血的铁之心", "染血的黑之羽", "骑士染血之时", "染血骑士之杯", "染血的铁假面"],
    ["魔女的炎之花", "魔女常燃之羽", "魔女破灭之时", "魔女的心之火", "焦灼的魔女帽"],
    ["角斗士的留恋", "角斗士的归宿", "角斗士的希冀", "角斗士的酣醉", "角斗士的凯旋"],
    ["饰金胸花", "追忆之风", "坚铜罗盘", "沉波之盏", "酒渍船帽"],
    ["渡火者的决绝", "渡火者的解脱", "渡火者的煎熬", "渡火者的醒悟", "渡火者的智慧"],
    ["远方的少女之心", "少女飘摇的思念", "少女苦短的良辰", "少女片刻的闲暇", "少女易逝的芳颜"],
    ["宗室之花", "宗室之翎", "宗室时计", "宗室银瓮", "宗室面具"],
    ["夏祭之花", "夏祭终末", "夏祭之刻", "夏祭水玉", "夏祭之面"],
    ["平雷之心", "平雷之羽", "平雷之刻", "平雷之器", "平雷之冠"],
    ["雷鸟的怜悯", "雷灾的孑遗", "雷霆的时计", "降雷的凶兆", "唤雷的头冠"],
    ["野花记忆的绿野", "猎人青翠的箭羽", "翠绿猎人的笃定", "翠绿猎人的容器", "翠绿的猎人之冠"],
    ["乐团的晨光", "琴师的箭羽", "终幕的时计", "吟游者之壶", "指挥的礼帽"],
    ["战狂的蔷薇", "战狂的翎羽", "战狂的时计", "战狂的骨杯", "战狂的鬼面"],
    ["勇士的勋章", "勇士的期许", "勇士的坚毅", "勇士的壮行", "勇士的冠冕"],
    ["守护之花", "守护徽印", "守护座钟", "守护之皿", "守护束带"],
    ["流放者之花", "流放者之羽", "流放者怀表", "流放者之杯", "流放者头冠"],
    ["赌徒的胸花", "赌徒的羽饰", "赌徒的怀表", "赌徒的骰盅", "赌徒的耳环"],
    ["教官的胸花", "教官的羽饰", "教官的怀表", "教官的茶杯", "教官的帽子"],
    ["武人的红花", "武人的羽饰", "武人的水漏", "武人的酒杯", "武人的头巾"],
    ["祭水礼冠"],
    ["祭火礼冠"],
    ["祭雷礼冠"],
    ["祭冰礼冠"],
    ["故人之心", "归乡之羽", "逐光之石", "异国之盏", "感别之冠"],
    ["学士的书签", "学士的羽笔", "学士的时钟", "学士的墨杯", "学士的镜片"],
    ["奇迹之花", "奇迹之羽", "奇迹之沙", "奇迹之杯", "奇迹耳坠"],
    ["冒险家之花", "冒险家尾羽", "冒险家怀表", "冒险家金杯", "冒险家头带"],
    ["幸运儿绿花", "幸运儿鹰羽", "幸运儿沙漏", "幸运儿之杯", "幸运儿银冠"],
    ["游医的银莲", "游医的枭羽", "游医的怀钟", "游医的药壶", "游医的方巾"],
    ["勋绩之花", "昭武翎羽", "金铜时晷", "盟誓金爵", "将帅兜鏊"],
    ["无垢之花", "贤医之羽", "停摆之刻", "超越之盏", "嗤笑之面"],
    ["祈望之心", "思忆之矢", "无常之面", "羁缠之花", "朝露之时"],
    ["绯花之壶", "切落之羽", "华饰之兜", "明威之镡", "雷云之笼"]
]
Users = [
    "空",
    "荧",
    "安柏",
    "凯亚",
    "丽莎",
    "琴",
    "可莉",
    "诺艾尔",
    "芭芭拉",
    "温迪",
    "雷泽",
    "迪卢克",
    "班尼特",
    "菲谢尔",
    "北斗",
    "凝光",
    "香菱",
    "行秋",
    "重云",
    "砂糖",
    "莫娜",
    "刻晴",
    "七七",
    "达达利亚",
    "迪奥娜",
    "钟离",
    "辛焱",
    "阿贝多",
    "甘雨",
    "魈",
    "胡桃",
    "罗莎莉亚",
    "烟绯",
    "尤拉",
]


TypeNamesGenshinArt = ["flower", "feather", "sand", "cup", "head"]
AttrNamesGensinArt = {
    "FIGHT_PROP_CRITICAL": "critical",
    "FIGHT_PROP_CRITICAL_HURT": "criticalDamage",
    "FIGHT_PROP_ATTACK": "attackStatic",
    "FIGHT_PROP_ATTACK_PERCENT": "attackPercentage",
    "FIGHT_PROP_ELEMENT_MASTERY": "elementalMastery",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "recharge",
    "FIGHT_PROP_HP": "lifeStatic",
    "FIGHT_PROP_HP_PERCENT": "lifePercentage",
    "FIGHT_PROP_DEFENSE": "defendStatic",
    "FIGHT_PROP_DEFENSE_PERCENT": "defendPercentage",
    "FIGHT_PROP_PHYSICAL_ADD_HURT": "physicalBonus",
    "FIGHT_PROP_HEAL_ADD": "cureEffect",
    "FIGHT_PROP_ROCK_ADD_HURT": "rockBonus",
    "FIGHT_PROP_WIND_ADD_HURT": "windBonus",
    "FIGHT_PROP_ICE_ADD_HURT": "iceBonus",
    "FIGHT_PROP_WATER_ADD_HURT": "waterBonus",
    "FIGHT_PROP_FIRE_ADD_HURT": "fireBonus",
    "FIGHT_PROP_ELEC_ADD_HURT": "thunderBonus",
    "FIGHT_PROP_GRASS_ADD_HURT": "grassBonus",
    "FIGHT_PROP_FIRE_SUB_HURT": "fireDeduct",
}
SetNamesGenshinArt = [
    "archaicPetra",  # 悠古的磐岩
    "blizzardStrayer",  # 冰风迷途的勇士
    "bloodstainedChivalry",  # 染血的骑士道
    "crimsonWitch",  # 炽烈的炎之魔女
    "gladiatorFinale",  # 角斗士的终幕礼
    "heartOfDepth",  # 沉沦之心
    "lavaWalker",  # 渡过烈火的贤人
    "maidenBeloved",  # 被怜爱的少女
    "noblesseOblige",  # 昔日宗室之仪
    "retracingBolide",  # 逆飞的流星
    "thunderSmoother",  # 平息雷鸣的尊者
    "thunderingFury",  # 如雷的盛怒
    "viridescentVenerer",  # 翠绿之影
    "wandererTroupe",  # 流浪大地的乐团
    "berserker",  # 战狂
    "braveHeart",  # 勇士之心
    "defenderWill",  # 守护之心
    "exile",  # 流放者
    "gambler",  # 赌徒
    "instructor",  # 教官
    "martialArtist",  # 武人
    "prayersForDestiny",  # 祭水之人
    "prayersForIllumination",  # 祭火之人
    "prayersForWisdom",  # 祭雷之人
    "prayersToSpringtime",  # 祭冰之人
    "resolutionOfSojourner",  # 行者之心
    "scholar",  # 学士
    "tinyMiracle",  # 奇迹
    "adventurer",  # 冒险家
    "luckyDog",  # 幸运儿
    "travelingDoctor",  # 游医
    "tenacityOfTheMillelith",  # 千岩牢固
    "paleFlame",  # 苍白之火
    "shimenawaReminiscence", # 追忆之注连
    "emblemOfSeveredFate", # 绝缘之旗印
]


TypeNamesMingyuLab = ['flower', 'plume', 'eon', 'goblet', 'circlet']
AttrNamesMingyuLab = {
    "FIGHT_PROP_CRITICAL": "critRate",
    "FIGHT_PROP_CRITICAL_HURT": "critDamage",
    "FIGHT_PROP_ATTACK": "flatATK",
    "FIGHT_PROP_ATTACK_PERCENT": "percentATK",
    "FIGHT_PROP_ELEMENT_MASTERY": "elementalMastery",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "energyRecharge",
    "FIGHT_PROP_HP": "flatHP",
    "FIGHT_PROP_HP_PERCENT": "percentHP",
    "FIGHT_PROP_DEFENSE": "flatDEF",
    "FIGHT_PROP_DEFENSE_PERCENT": "percentDEF",
    "FIGHT_PROP_PHYSICAL_ADD_HURT": "physicalDamage",
    "FIGHT_PROP_HEAL_ADD": "healing",
    "FIGHT_PROP_ROCK_ADD_HURT": "geoDamage",
    "FIGHT_PROP_WIND_ADD_HURT": "anemoDamage",
    "FIGHT_PROP_ICE_ADD_HURT": "cryoDamage",
    "FIGHT_PROP_WATER_ADD_HURT": "hydroDamage",
    "FIGHT_PROP_FIRE_ADD_HURT": "pyroDamage",
    "FIGHT_PROP_ELEC_ADD_HURT": "electroDamage",
    "FIGHT_PROP_GRASS_ADD_HURT": "dendroDamage",
    "FIGHT_PROP_FIRE_SUB_HURT": "pyroDEF",
}

SetNamesMingyuLab = [
    "archaic_petra",  # 悠古的磐岩
    "blizzard_walker",  # 冰风迷途的勇士
    "bloodstained_chivalry",  # 染血的骑士道
    "crimson_witch_of_flames",  # 炽烈的炎之魔女
    "gladiators_finale",  # 角斗士的终幕礼
    "heart_of_depth",  # 沉沦之心
    "lavawalker",  # 渡过烈火的贤人
    "maiden_beloved",  # 被怜爱的少女
    "noblesse_oblige",  # 昔日宗室之仪
    "retracing_bolide",  # 逆飞的流星
    "thundersoother",  # 平息雷鸣的尊者
    "thundering_fury",  # 如雷的盛怒
    "viridescent_venerer",  # 翠绿之影
    "wanderers_troupe",  # 流浪大地的乐团
    "berserker",  # 战狂
    "brave_heart",  # 勇士之心
    "defenders_will",  # 守护之心
    "the_exile",  # 流放者
    "gambler",  # 赌徒
    "instructor",  # 教官
    "martial_artist",  # 武人
    "prayers_of_destiny",  # 祭水之人
    "prayers_of_illumination",  # 祭火之人
    "prayers_of_wisdom",  # 祭雷之人
    "prayers_of_springtime",  # 祭冰之人
    "resolution_of_sojourner",  # 行者之心
    "scholar",  # 学士
    "tiny_miracle",  # 奇迹
    "adventurer",  # 冒险家
    "lucky_dog",  # 幸运儿
    "traveling_doctor",  # 游医
    "tenacity_of_the_millelith",  # 千岩牢固
    "pale_flame",  # 苍白之火
    "reminiscence_of_shime", # 追忆之注连
    "seal_of_insulation", # 绝缘之旗印
]