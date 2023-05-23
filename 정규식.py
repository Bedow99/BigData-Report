import re

# 이메일의 패턴 검색 후 출력
pattern = re.compile(r'\w+@\w+\.[a-zA-Z]{2,4}')
text = '테스트 이메일 주소 test@gmail.com.'
email = pattern.search(text)
if email:
  print('이메일의 패턴이 있을 경우 해당 텍스트와 이메일이 출력됩니다.')
  print(email.group() + '\n')
else:
  print('이메일의 패턴이 없을 경우 해당 텍스트가 출력됩니다.\n')

# 전화번호 추출
pattern = re.compile(r'\d{2,3}-\d{3,4}-\d{4}')
text = '테스트 전화번호는 010-9999-1234입니다.'
phone = pattern.search(text)
if phone:
  print('전화번호의 패턴과 맞을 시 해당 텍스트와 전화번호가 출력됩니다.')
  print(phone.group() + '\n')
else:
  print('전화번호의 패턴과 맞지 않을 시 해당 텍스트가 출력됩니다.\n')

# 문자열 대체
pattern = re.compile(r'My')
text = 'My name is James'
new_text = pattern.sub('Your', text)
print('입력된 텍스트에 "My"가 포함되어 있을 경우 "My"가 "Your"로 변환되어 출력됩니다.')
print(new_text)
