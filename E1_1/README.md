# Codyssey E1-1 개발 워크스테이션 구축

## 1. 프로젝트 개요

이 프로젝트는 개발 워크스테이션을 직접 구성하면서 Linux CLI, Docker, Git/GitHub의 기본 흐름을 실습하고 기록하는 프로젝트이다.

현재까지 터미널에서 파일과 디렉터리를 생성·복사·이동·삭제했고, macOS·Shell·Git·Docker 실행 환경을 확인했다. 파일 및 디렉터리 권한 실습은 다음 단계에서 실제 명령과 결과를 기록할 예정이다.

### 미션 목표

- CLI를 사용해 파일과 디렉터리를 생성·복사·이동·삭제한다.
- 절대 경로와 상대 경로의 차이를 설명한다.
- 파일 권한 `r/w/x`와 숫자 권한 `644`, `755`를 설명한다.
- Docker 이미지와 컨테이너의 차이를 설명한다.
- 기존 Nginx 이미지를 기반으로 커스텀 이미지를 만든다.
- 포트 매핑을 이용해 컨테이너의 웹 서버에 접속한다.
- 바인드 마운트로 호스트 파일 변경이 즉시 반영되는지 확인한다.
- Docker 볼륨으로 컨테이너 삭제 후에도 데이터가 유지되는지 확인한다.
- Git과 GitHub를 이용해 결과물을 기록하고 공유한다.

---

## 2. 실행 환경

| 항목 | 환경 |
|---|---|
| Host OS | macOS 15.7.4 (Build 24G517) |
| Shell | zsh (`/bin/zsh`) |
| Terminal | macOS Terminal |
| Editor | Visual Studio Code |
| Docker 실행 환경 | OrbStack (`orbstack` context) |
| Docker Client | 28.5.2 (build ecc6942) |
| Git | 2.53.0 |
| 기본 작업 브랜치 | `main` |

다음 명령으로 실제 실행 환경을 확인했다.

```bash
sw_vers
echo $SHELL
git --version
docker --version
docker info
```

확인 결과:

```text
ProductName:      macOS
ProductVersion:   15.7.4
BuildVersion:     24G517

/bin/zsh
git version 2.53.0
Docker version 28.5.2, build ecc6942
Docker Context: orbstack
```

![실행 환경 확인](https://raw.githubusercontent.com/Kfri-cloud/codyssey-onboarding-e1-1-development-workstation/main/screenshots/01-environment.png)

> 처음에 `sw vers`를 입력해 `zsh: command not found: sw` 오류가 발생했다. macOS 버전 확인 명령은 공백이 아닌 밑줄을 사용하는 `sw_vers`이므로 명령을 수정해 정상적으로 확인했다.

---

## 3. 프로젝트 구조

```text
Codyssey/
├── README.md
└── E1_1/
    └── README.md
```

현재는 Docker 실습 전 단계까지만 문서화했다. 이후 실습을 진행하면서 `terminal-practice`, `permission-practice`, `docs/logs`, `docs/images` 등의 결과 파일을 추가할 예정이다.

---

## 4. 수행 체크리스트

- [x] 저장소 및 프로젝트 디렉터리 구성
- [x] OS, Shell, Docker, Git 환경 확인
- [x] 터미널 기본 명령 실습
- [x] 절대 경로와 상대 경로 확인
- [ ] 파일 및 디렉터리 권한 변경
- [x] Git 사용자 정보와 기본 브랜치 `main` 설정 확인
- [x] GitHub 원격 저장소 연결 확인
- [ ] Docker 기본 실습 이후 항목

---

## 5. 터미널 기본 조작

### 5.1 수행 명령

```bash
pwd
mkdir -p ~/codyssey/practice
cd ~/codyssey/practice
ls -la

touch original.txt
echo "Codyssey CLI practice" > original.txt
cat original.txt

cp original.txt coide.txt
mv coide.txt renamed.txt
mkdir sample-directory
ls -la

rm renamed.txt
rmdir sample-directory
ls -la
```

### 5.2 검증 결과

- `pwd`로 현재 작업 위치를 확인했다.
- `mkdir -p ~/codyssey/practice`로 실습 디렉터리를 만들었다.
- `ls -la`로 숨김 항목과 파일의 상세 정보를 확인했다.
- `touch`와 `echo`로 파일을 만들고 내용을 기록했다.
- `cat`으로 파일에 저장된 내용을 확인했다.
- `cp`로 파일을 복사하고 `mv`로 이름을 변경했다.
- `rm`으로 파일을 삭제하고 `rmdir`로 빈 디렉터리를 삭제했다.

실제 확인한 내용:

```text
$ pwd
/Users/[사용자명]

$ mkdir -p
usage: mkdir [-pv] [-m mode] directory_name ...

$ mkdir -p~/codyssey/practice
mkdir: illegal option -- ~

$ mkdir -p ~/codyssey/practice

$ cd ~codysseypractice
zsh: no such user or named directory: codysseypractice

$ cd ~/codyssey/practice
$ ls -la
total 0
drwxr-xr-x  2 [사용자명]  [그룹명]  64  8  4 16:46 .
drwxr-xr-x  3 [사용자명]  [그룹명]  96  8  4 16:46 ..

$ touch original.txt
$ echo "Codyssey CLI practice" > original.txt
$ cat original.txt
Codyssey CLI practice

$ cp original.txt coide.txt
$ mv coide.txt renamed.txt
$ mkdir sample-directory
$ rm renamed.txt

$ rmdir samplre-directory
rmdir: samplre-directory: No such file or directory

$ rmdir sample-directory
```

오류를 통해 다음 내용을 확인했다.

1. `mkdir -p` 뒤에는 생성할 경로가 필요하다.
2. 옵션과 경로 사이에는 공백을 넣어야 한다.
3. 홈 디렉터리 아래 경로는 `~/codyssey/practice`처럼 슬래시로 구분한다.
4. 파일 또는 디렉터리 이름을 잘못 입력하면 `No such file or directory` 오류가 발생한다.

### 5.3 절대 경로와 상대 경로

- **절대 경로**는 파일 시스템의 최상위 위치부터 대상을 표현한 전체 경로다.
- **상대 경로**는 현재 작업 디렉터리를 기준으로 대상을 표현한다.

```text
절대 경로: /Users/[사용자명]/codyssey/practice/original.txt
상대 경로: ./original.txt
```

절대 경로는 현재 위치가 달라져도 같은 대상을 가리킨다. 상대 경로는 현재 위치에 따라 가리키는 대상이 달라질 수 있다.

---

## 6. 파일 및 디렉터리 권한

### 6.1 권한 의미

| 권한 | 파일에서의 의미 | 디렉터리에서의 의미 | 숫자 |
|---|---|---|---:|
| `r` | 내용 읽기 | 목록 확인 | 4 |
| `w` | 내용 수정 | 파일 생성·삭제 | 2 |
| `x` | 파일 실행 | 디렉터리 내부 접근 | 1 |

권한은 소유자(User), 그룹(Group), 기타 사용자(Others) 순서로 표시된다.

```text
644 = rw-r--r--
755 = rwxr-xr-x
600 = rw-------
700 = rwx------
```

디렉터리의 `x`는 프로그램 실행이 아니라 디렉터리 안으로 들어가거나 내부 항목에 접근할 수 있는 권한을 의미한다.

### 6.2 수행 예정 명령

```bash
mkdir -p permission-practice
touch permission-practice/my-file.txt
mkdir permission-practice/my-directory

chmod 700 permission-practice/my-directory
chmod 600 permission-practice/my-file.txt
ls -ld permission-practice/my-file.txt permission-practice/my-directory

chmod 755 permission-practice/my-directory
chmod 644 permission-practice/my-file.txt
ls -ld permission-practice/my-file.txt permission-practice/my-directory
```

### 6.3 결과 기록

권한 실습을 실행한 뒤 아래 부분을 실제 출력으로 교체한다.

```text
# TODO: 600/700 변경 결과
# TODO: 644/755 변경 결과
```

예상되는 최종 권한은 다음과 같다.

```text
디렉터리: drwxr-xr-x = 755
파일:     -rw-r--r-- = 644
```

> 여기까지 Docker 실습 전 단계의 기록이다. Docker 설치 및 기본 점검부터는 실제 실습을 진행한 뒤 이어서 작성한다.
