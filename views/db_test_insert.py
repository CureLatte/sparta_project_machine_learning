from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient
import uuid
import datetime
import hashlib
import jwt


client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon


#비밀번호 해쉬

# pw_hash = hashlib.sha256('qwer1234'.encode('utf-8')).hexdigest()
#
# db.users.update_one({'user_id': 'qwer3'}, {'$set': {'password': 'qwer1234'}})


# a = {
#     'avatar': 'default',
#     'user_id': 'qwer2',
#     'password': 'qwer1234',
#     'phone_number': '010-2345-6789',
#     'gender': '여자',
#     'interest_poket': '파이리',
#     'point': 5000,
#     'poket_box': ['img']
# }
#
# b = {'poket_category':
#     [
#         '피카츄',
#         '라이츄',
#         '파이리',
#         '꼬부기'
#     ]
# }

i = uuid.uuid1()
today = datetime.datetime.now()
today_time = today.strftime('%Y-%m-%d %OH:%OM:%OS')

c = {
    'maket_id': str(i),
    'user_id': 'qwer1',
    'content': '작성글2',
    'comment':
        [
            {
                'photo_user_id': 'qwer3',
                'photo_comment': '안녕하세요',
                'photo_avatar': '작성자 avata3r'
            },
{
                'photo_user_id': 'qwer1',
                'photo_comment': '댓글 입니다',
                'photo_avatar': '작성자 avatar1'
            },
{
                'photo_user_id': 'qwer2',
                'photo_comment': '그렇쿤요',
                'photo_avatar': '작성자 avatar2'
            },
            {
                'photo_user_id': 'qwer4',
                'photo_comment': '아 네',
                'photo_avatar': '작성자 avatar4'
            }
        ],
    'category': '카테고리',
    'photo': 'img',
    'desc': '청도 프리미엄 특 왕 반건시 VIP 감동 선물세트',
    'header': '제목2',
    'date': today_time,
    'price': 1500
}

# db.users.insert_one(a)

# db.category.insert_one(b)

db.market.insert_one(c)


# -----------------------------------------------------------------포켓몬149 업로드
poket_all_class = {  # A
    0: '케이시',
    1: '프테라',
    2: '후딘',
    3: '얼음고지',
    4: '아보크',
    5: '윈디',
    6: '프리저',
    # B
    7: '독침붕',
    8: '모다피',
    9: '거북왕',
    10: '이상해씨',
    11: '버터플',
    # C
    12: '캐터피',
    13: '럭키',
    14: '리자몽',
    15: '파이리',
    16: '리자드',
    17: '픽시',
    18: '삐삐',
    19: '파르셀',
    20: '탕구리',
    # D
    21: '쥬레곤',
    22: '디그다',
    23: '메타몽',
    24: '두트리오',
    25: '두두',
    26: '신뇽',
    27: '망나뇽',
    28: '미뇽',
    29: '슬리프',
    30: '닥트리오',
    # E
    31: '이브이',
    32: '아보',
    33: '에레브',
    34: '붐볼',
    35: '아라리',
    36: '나시',
    # F
    37: '파오리',
    38: '깨비드릴조',
    39: '부스터',
    # G
    40: '고오스',
    41: '팬텀',
    42: '꼬마돌',
    43: '냄새꼬',
    44: '골뱃',
    45: '콘치',
    46: '골덕',
    47: '딱구리',
    48: '데구리',
    49: '질퍽이',
    50: '가디',
    51: '갸라도스',
    # H
    52: '고우스트',
    53: '홍수몬',
    54: '시라소몬',
    55: '쏘드라',
    56: '슬리퍼',
    # I
    57: '이상해풀',
    58: '푸린',
    59: '쥬피썬더',
    60: '루주라',
    # K
    61: '투구',
    62: '투구푸스',
    63: '윤겔라',
    64: '딱충이',
    65: '캥카',
    66: '킹크랩',
    67: '또가스',
    68: '크랩',
    # L
    69: '라프라스',
    70: '내루미',
    # M
    71: '괴력몬',
    72: '근육몬',
    73: '알통몬',
    74: '잉어킹',
    75: '마그마',
    76: '코일',
    77: '레어코일',
    78: '망키',
    79: '텅구리',
    80: '나옹',
    81: '단데기',
    82: '뮤',
    83: '뮤츠',
    84: '파이어',
    85: '마임맨',
    86: '질뻐기',
    # N
    87: '니드킹',
    88: '니드퀸',
    89: '니드리나',
    90: '니드리노',
    91: '나인테일',
    # O
    92: '뚜벅쵸',
    93: '암나이트',
    94: '암스타',
    95: '롱스톤',
    # P
    96: '파라스',
    97: '파라섹트',
    98: '페르시온',
    99: '피죤',
    100: '피죤투',
    101: '구구',
    102: '피카츄',
    103: '쁘사이저',
    104: '발챙이',
    105: '슈륙챙이',
    106: '강챙이',
    107: '포니타',
    108: '폴리곤',
    109: '성원숭',
    110: '고라파덕',
    # R
    111: '라이츄',
    112: '날쌩마',
    113: '레트라',
    114: '꼬렛',
    115: '코뿌리',
    116: '뿔카노',
    # S
    117: '모래두지',
    118: '고지',
    119: '스라크',
    120: '시드라',
    121: '왕콘치',
    122: '쥬쥬',
    123: '셀러',
    124: '야도란',
    125: '야돈',
    126: '잠만보',
    127: '깨비참',
    128: '꼬부기',
    129: '아쿠스타',
    130: '별가사리',
    # T
    131: '덩쿠리',
    132: '켄타우로스',
    133: '왕눈해',
    134: '독파리',
    # V
    135: '샤미드',
    136: '도나리',
    137: '콘팡',
    138: '이상해 꽃',
    139: '우츠보트',
    140: '라플레시아',
    141: '찌리리공',
    142: '식스테일',
    # W
    143: '어니부기',
    144: '뿔충이',
    145: '우츠동',
    146: '또도가스',
    147: '푸크린',
    148: '썬더',
    149: '주뱃'
}


n = {'poket_category': list(poket_all_class.values())}

db.category.insert_one(n)