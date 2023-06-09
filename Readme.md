# 정규 표현식 (Regular Expression), 가비지 컬렉션(Garbage Collection)에 대한 이해와 예시

## 정규 표현식(Regular Expression)의 정의
프로그래밍에서 문자열을 다룰 때, 문자열의 일정한 패턴을 표현하는 일종의 형식 언어를 의미합니다. 정규식이라고도 부르며, 보통 RegEx 혹은 RegExp라 많이 쓰입니다.

## 이해한 내용
정규 표현식은 이메일, 전화번호, 생년월일등 특정한 형식을 가진 문자열, 데이터를 가공, 추출, 검색등을 하기 위해 사용되며, 이를 통해 자료에 필요한 부분이 누락되었는지, 또는 특정 부분이 포함되었는지 확인 할 수 있습니다.
실제로 비밀번호의 규격을 정하거나 이메일을 규격을 확인하는 등 많이 쓰이고 있습니다.


## Python 코드 예시
파이썬에서 정규 표현식을 사용하기 위해 're'모듈을 임포트하여 사용해야 합니다.
![정규식 표현](https://github.com/Bedow99/BigData-Report/assets/102810983/4c780db1-a8f2-40b7-b1da-81d8fa417fb8)

## 가비지 컬렉션(Garbage Collection)의 정의
프로그래밍 언어의 메모리 관리 기법 중 하나로 프로그램이 동적으로 할당한 메모리 중에서 더 이상 사용되지 않는 객체 또는 메모리 블록을 자동으로 탐지하여 해제하는 과정을 말합니다.

## 이해한 내용
가비지 컬렉션은 더 이상 사용되지 않거나, 참조하는 것이 전무 한 데이터가 생겼을 때 그 데이터를 가비지로 모으고 가비지 컬렉션을 통해 자동적으로 찾아내고 삭제하여 메모리 누수를 막는 것을 의미합니다.
이는 메모리가 제한적인 컴퓨터 환경에서 사용되었을 경우 시스템의 성능 향상을 기대 할 수 잇습니다.

## Python 코드 예시
가비지 컬렉션이 제대로 작동하기 위해서는 순환참조를 지양해야하고 사용이 끝난 외부 리소스는 메서드를 호출하여 외부 리소스를 해제 시켜줘야 합니다.
또한 데이터에 대한 개발자의 적절한 조치가 필요합니다. ex)데이터가 많을(대용량 데이터) 경우 스트림을 사용합니다.

가비지 컬렉션이 제대로 작동하지 않고 메모리 누수가 계속해서 발생되는 경우는 위의 경우를 위반한 경우입니다.

다음 코드는 순환참조를 통해 가비지 컬렉션이 제대로 작동하지 않는 예시(위 2줄)와 그 해결법(아래 2줄)입니다.
![가비지 컬렉션](https://github.com/Bedow99/BigData-Report/assets/102810983/0da41c5c-d07c-4e8f-8dcb-2e3bc0dba93f)

