# Cloth_Hanger


딥러닝 기반 여성의류 분류 시스템

## 개발환경

Ubuntu 12.04

Django version 2.1.2

Python version 3.7.3

pytorch version 1.1.0

torchvision 0.3.0

pandas 0.24.2

miniconda 개발환경 사용

## 설치방법

git clone으로 모든 데이터를 다운받는다, 단, 'management' 폴더 안에 있는 classification_model 데이터는 git lfs로 저장했기 때문에 clone으로는 다운되지 않는다. 따로 선택해 다운받아야 한다.

(classification_model의 정상적인 데이터 크기는 약 500MB로, git clone으로 다운받았을 시에는 이 크기보다 한참 작은 값이 로딩되어 있다.)

### Windows

anaconda3 설치 (https://www.anaconda.com/distribution/)

설치 후 anaconda prompt를 열고

```
conda install -c anaconda django

conda install -c anaconda sqlparse

conda install -c pytorch pytorch

conda install -c pytorch torchvision
```

로 django 및 pytorch를 설치한다.

이후 src로 디렉토리를 이동한 다음

```python
./manage.py makemigrations management

./manage.py migrate

./manage.py runserver 0.0.0.0:8080

```
명령어를 순차적으로 실행해 로컬서버를 구동한다.
