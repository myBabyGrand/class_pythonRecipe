import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('myKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://python-recipe-default-rtdb.firebaseio.com'
})

# ref = db.reference() #db 위치 지정
# ref.update({'majorTom' : 'Astronaut'}) #해당 변수가 없으면 생성한다.
#
# ref = db.reference('class/python') #db 위치 지정
# ref.update({'python Recipe' : 'complete'})
# ref.update({'python application ' : 'ready'})
#
# ## list
# ref = db.reference() #db 위치 지정
# ref.update({'completed class' : ['스프링 MVC 1', '스프링 MVC 2', '스프링 DB 1', '스프링 DB 2', '스프링 데이터 JPA']})


# 조회

#데이터베이스 레퍼런스 생성 후 데이터 읽기
ref = db.reference('XXXX') #이 당시의 데이터가 확인된다.
print(ref.get()) #특정값이 가져와지거나

ref = db.reference('majorTom')
print(ref.get())

ref = db.reference('class/python')
print(ref.get()) #json형태로 받아와 진다.

ref = db.reference('completed class')
print(ref.get()) #list로 반환

