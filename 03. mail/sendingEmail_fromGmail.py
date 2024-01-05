import smtplib
from email.mime.text import MIMEText
from datetime import datetime




sendEmail = "glenn.aws01@gmail.com"
recvEmail = "6pmfriday@gmail.com"
password = "" ##App 비밀번호

smtpName = "smtp.gmail.com" #smtp 서버 주소
smtpPort = 587 #smtp 포트 번호

#본문
from email.mime.multipart import MIMEMultipart

#여러 MIME을 넣기위한 MIMEMultipart 객체 생성
msg = MIMEMultipart()

msg['Subject'] ='메일제목 '+str(datetime.now())
msg['From'] = sendEmail
msg['To'] = recvEmail
text = "메일 본문입니다"
contentPart = MIMEText(text) #MIMEText(text , _charset = "utf8")

msg.attach(contentPart)


#파일 추가
from email.mime.application import MIMEApplication
etcFileName = 'README_copy.md'
with open(etcFileName, 'rb') as etcFD :
    etcPart = MIMEApplication( etcFD.read() )
    #첨부파일의 정보를 헤더로 추가
    etcPart.add_header('Content-Disposition','attachment', filename=etcFileName)
    msg.attach(etcPart)


s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
s.starttls() #TLS 보안 처리
s.login( sendEmail , password ) #로그인
s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환해야 합니다.
s.close() #smtp 서버 연결을 종료합니다