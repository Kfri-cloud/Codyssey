# Codyssey E1-1 개발 워크스테이션 구축

## 1. 프로젝트 개요

이 프로젝트는 개발 워크스테이션을 직접 구성하면서 Linux CLI, Docker, Git/GitHub의 기본 흐름을 실습한 결과물이다.

터미널에서 파일과 디렉터리를 관리하고, macOS에서 OrbStack을 이용해 Docker 컨테이너를 실행했다. `hello-world`, Ubuntu, Nginx, MySQL 컨테이너를 직접 생성하고 이미지·컨테이너 조회, 로그 확인, 포트 매핑, 컨테이너 내부 접근, 삭제, 바인드 마운트에 따른 데이터 유지 여부를 검증했다.

### 기존 실습 저장소에서 가져온 근거

이 문서는 먼저 수행한 [개발 워크스테이션 실습 저장소](https://github.com/Kfri-cloud/codyssey-onboarding-e1-1-development-workstation)의 실제 명령 결과와 마스킹된 증거 자료를 함께 활용해 구성했다. 기존 자료에 실제 출력이 있는 항목만 완료 근거로 사용했으며, TODO로 남아 있거나 실행 출력이 없는 항목은 보완 필요 상태로 유지했다.

- [기존 저장소의 hello-world 및 Docker 실습 커밋](https://github.com/Kfri-cloud/codyssey-onboarding-e1-1-development-workstation/commit/edcab3c7e44d7e23351cb370ab52962b9a85e68a)
- [기존 저장소의 마스킹된 Docker 증거 커밋](https://github.com/Kfri-cloud/codyssey-onboarding-e1-1-development-workstation/commit/6b0a824432b57846478a82691d4a584b644ceca2)
- [기존 저장소의 Git 설정 및 브랜치 복구 기록](https://github.com/Kfri-cloud/codyssey-onboarding-e1-1-development-workstation/commit/b558097e2aceeb6da5c276ffa6ebd7736ca266e7)

### 미션 목표

- CLI로 파일과 디렉터리를 생성·복사·이동·삭제한다.
- 절대 경로와 상대 경로의 차이를 설명한다.
- 파일과 디렉터리 권한의 의미를 설명한다.
- Docker 이미지와 컨테이너의 차이를 설명한다.
- 컨테이너를 생성·실행·중지·삭제한다.
- 포트 매핑으로 컨테이너의 웹 서버에 접속한다.
- 바인드 마운트와 Docker 볼륨의 차이를 설명한다.
- Git과 GitHub를 이용해 실습 결과를 기록하고 공유한다.

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
| 기본 브랜치 | `main` |

```bash
sw_vers
echo $SHELL
git --version
docker --version
docker info
```

![실행 환경 확인](./docs/images/01-environment.png)

처음에는 `sw vers`와 `doker info`처럼 명령을 잘못 입력해 오류가 발생했다. 각각 `sw_vers`, `docker info`로 수정해 정상적으로 실행했다.

- [Docker 환경 확인 로그](./docs/logs/docker/info.txt)

---

## 3. 프로젝트 구조

```text
E1-1/
├── README.md
└── docs/
    ├── images/
    │   ├── 01-environment.png
    │   ├── 02-directory-created.png
    │   ├── 03-file-copy-rename.png
    │   ├── 04-file-delete.png
    │   ├── 05-directory-delete.png
    │   ├── 06-docker-client.png
    │   ├── 07-docker-server.png
    │   ├── 08-hello-world.png
    │   ├── 09-ubuntu-practice.png
    │   ├── 10-background-name-error.png
    │   ├── 11-docker-hello-world-masked.png
    │   ├── 11-git-config.png
    │   └── 12-github-remote.png
    └── logs/
        └── docker/
            ├── info.txt
            ├── hello_world.txt
            ├── Ubuntu_1.txt
            ├── Ubuntu_2.txt
            └── docker_practice/
                ├── docker_container_create_del.txt
                ├── docker_exec -it
                ├── docker_image.txt
                ├── docker_logs
                ├── docker_mapping
                ├── docker_nginx.txt
                ├── docker_volume
                └── docker_volume_Non
        └── git/
            └── push_evidence.md
```

---

## 4. 평가 기준 대응 현황

| 평가 항목 | 상태 | 확인 근거 |
|---|---|---|
| 터미널 폴더·파일 생성·이동·삭제 | 완료 | 5번 실습 명령 및 이미지 02~05 |
| 파일 및 디렉터리 권한 변경 | 보완 필요 | 개념과 실행 명령은 있으나 실제 `chmod` 출력 로그 미확인 |
| Docker 버전 및 동작 상태 | 보완 필요 | 버전과 이미지 증거는 있으나 `docker info` Server 전체 텍스트 로그 추가 필요 |
| `hello-world` 실행 | 완료 | `Hello from Docker!`, `Exited (0)`, 이미지 08 |
| 이미지·컨테이너 확인 및 정리 | 완료 | `image ls`, `ps -a`, `stop`, `rm`, `rm -f` 로그 |
| Dockerfile 이미지 빌드 | 보완 필요 | `Dockerfile`과 `docker build` 결과 미확인 |
| 포트 매핑 및 접속 | 보완 필요 | `-p 4000:80` 매핑은 확인했으나 `curl` 또는 브라우저 접속 증거 추가 필요 |
| 컨테이너 삭제 후 데이터 유지 | 보완 필요 | 재연결 후 `mydb`는 확인했으나 삭제 명령을 포함한 연속 로그 추가 필요 |
| Git 설정 및 GitHub 연동 | 완료 | Git 설정·원격 저장소 이미지와 실제 원격 커밋 기록 |

> 권한 변경과 Dockerfile 빌드는 실제 출력이 없어 보완 대상으로 남겼다. MySQL은 같은 바인드 마운트에서 `mydb`가 다시 조회됐지만 삭제 명령 출력이 빠져 있으므로 완전한 연속 로그를 추가한 뒤 완료 처리한다.

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

rm renamed.txt
rmdir sample-directory
ls -la
```

### 5.2 검증 결과

- `pwd`로 현재 위치를 확인했다.
- `mkdir -p`로 중간 경로를 포함한 실습 디렉터리를 생성했다.
- `touch`와 `echo`로 파일을 생성하고 내용을 기록했다.
- `cp`로 파일을 복사하고 `mv`로 이름을 변경했다.
- `rm`으로 파일을, `rmdir`로 빈 디렉터리를 삭제했다.
- 명령 옵션과 경로 사이에 공백이 필요하다는 것을 오류를 통해 확인했다.

### 5.3 실습 이미지

디렉터리 생성:

![디렉터리 생성](./docs/images/02-directory-created.png)

파일 복사 및 이름 변경:

![파일 복사 및 이름 변경](./docs/images/03-file-copy-rename.png)

파일 삭제:

![파일 삭제](./docs/images/04-file-delete.png)

빈 디렉터리 삭제:

![디렉터리 삭제](./docs/images/05-directory-delete.png)

### 5.4 절대 경로와 상대 경로

- **절대 경로**: 파일 시스템의 최상위 위치부터 작성한 전체 경로
- **상대 경로**: 현재 작업 디렉터리를 기준으로 작성한 경로

```text
절대 경로: /Users/[사용자명]/codyssey/practice/original.txt
상대 경로: ./original.txt
```

---

## 6. 파일 및 디렉터리 권한

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

디렉터리의 `x`는 프로그램 실행이 아니라 디렉터리 내부에 접근할 수 있는 권한이다.

현재 저장소에는 권한 변경 결과 로그가 없으므로, 다음 실습 후 실제 출력 결과를 추가해야 한다.

```bash
chmod 700 permission-practice/my-directory
chmod 600 permission-practice/my-file.txt
ls -ld permission-practice/my-file.txt permission-practice/my-directory

chmod 755 permission-practice/my-directory
chmod 644 permission-practice/my-file.txt
ls -ld permission-practice/my-file.txt permission-practice/my-directory
```

---

## 7. Docker 설치 및 기본 점검

### 7.1 Client와 Server

- **Docker Client**는 사용자가 입력한 `docker` 명령을 Docker 엔진에 전달한다.
- **Docker Server(Daemon)**는 이미지 다운로드, 컨테이너 생성 및 실행을 실제로 처리한다.
- `docker info`에서 Client와 Server 정보가 모두 출력되면 Docker 엔진이 실행 중인 상태다.

![Docker Client 확인](./docs/images/06-docker-client.png)

![Docker Server 확인](./docs/images/07-docker-server.png)

### 7.2 이미지와 컨테이너

| 구분 | 이미지 | 컨테이너 |
|---|---|---|
| 의미 | 실행 환경을 만드는 읽기 전용 설계도 | 이미지를 기반으로 실제 실행된 환경 |
| 상태 | 실행되지 않음 | 실행·중지·삭제 가능 |
| 관계 | 하나의 이미지로 여러 컨테이너 생성 가능 | 생성할 때 특정 이미지를 사용 |

```text
Image → Container 생성 → 실행 → 중지 → 삭제
```

---

## 8. hello-world 실행

```bash
docker run --name hello-test hello-world
docker images
docker ps
docker ps -a --filter name=hello-test
```

`Hello from Docker!` 메시지와 `Exited (0)` 상태를 통해 컨테이너가 오류 없이 작업을 마치고 종료된 것을 확인했다.

- `docker ps`: 현재 실행 중인 컨테이너만 표시
- `docker ps -a`: 종료된 컨테이너를 포함해 모두 표시
- `Exited (0)`: 명령을 정상적으로 끝내고 종료됨

![hello-world 실행 결과](./docs/images/08-hello-world.png)

![개인정보를 가린 hello-world 결과](./docs/images/11-docker-hello-world-masked.png)

- [hello-world 전체 stdout 및 Exited (0) 로그](./docs/logs/docker/hello_world.txt)

---

## 9. Ubuntu 컨테이너 실습

### 9.1 백그라운드 실행

```bash
docker run -dit --name ubuntu-practice00 ubuntu:24.04 bash
docker ps --filter name=ubuntu-practice00
docker exec ubuntu-practice00 pwd
docker exec ubuntu-practice00 ls -la /
docker exec ubuntu-practice00 cat /etc/os-release
```

Ubuntu 24.04.4 LTS 컨테이너가 백그라운드에서 실행됐으며, 컨테이너 내부의 시작 위치가 `/`임을 확인했다.

![Ubuntu 컨테이너 실습](./docs/images/09-ubuntu-practice.png)

- [Ubuntu 실행 및 내부 확인 로그](./docs/logs/docker/Ubuntu_1.txt)
- [Ubuntu 추가 실습 로그](./docs/logs/docker/Ubuntu_2.txt)

### 9.2 컨테이너 내부 파일 생성

```bash
docker exec ubuntu-practice00 sh -c \
  'echo "Hello from Ubuntu container" > /tmp/hello.txt'
docker exec ubuntu-practice00 cat /tmp/hello.txt
```

`sh -c`를 사용하는 이유는 출력 리다이렉션 `>`까지 컨테이너 내부의 Shell에서 해석하도록 만들기 위해서다.

### 9.3 오류 확인

```text
exec: "ls-la": executable file not found in $PATH
```

`ls-la`는 하나의 명령으로 해석되지만 그런 실행 파일은 존재하지 않는다. `ls -la`처럼 명령과 옵션 사이에 공백을 넣어 해결했다.

---

## 10. 컨테이너 생성·실행·중지·삭제

```bash
docker create nginx
docker ps -a
docker start <컨테이너_ID>
docker stop <컨테이너_ID>
docker rm <컨테이너_ID>
docker rm -f <실행_중인_컨테이너_ID>
```

- `docker create`: 컨테이너만 생성하고 실행하지 않는다.
- `docker start`: 생성 또는 중지된 컨테이너를 실행한다.
- `docker stop`: 실행 중인 컨테이너를 정상 중지한다.
- `docker rm`: 중지된 컨테이너를 삭제한다.
- `docker rm -f`: 실행 중인 컨테이너를 강제로 중지하고 삭제한다.

실행 중인 컨테이너를 일반 `docker rm`으로 삭제하려 하자 오류가 발생했고, `docker rm -f`로 정리했다.

- [컨테이너 생성·삭제 전체 로그](./docs/logs/docker/docker_practice/docker_container_create_del.txt)

---

## 11. 이미지 관리

```bash
docker pull nginx:alpine
docker image ls
docker image rm <이미지_ID>
```

Nginx의 `latest`와 `alpine` 이미지를 비교했을 때 실습 당시 크기는 각각 약 161MB와 62.4MB였다. Alpine 기반 이미지는 더 작은 Linux 배포판을 사용하므로 상대적으로 용량이 작다.

> `docker images ls`가 아니라 `docker images` 또는 `docker image ls`를 사용해야 한다.

- [이미지 다운로드·조회·삭제 로그](./docs/logs/docker/docker_practice/docker_image.txt)

---

## 12. Nginx 컨테이너와 내부 접근

```bash
docker run -d nginx
docker ps
docker exec -it <컨테이너_ID> bash
cd /etc/nginx
ls
cat nginx.conf
```

`docker exec -it`로 실행 중인 컨테이너에 새로운 대화형 Bash 프로세스를 실행했다. `/etc/nginx/nginx.conf`를 읽어 Nginx 설정 구조를 확인했다.

처음에는 `cat nginx,conf`처럼 쉼표를 입력해 파일을 찾을 수 없었고, 정확한 파일명인 `nginx.conf`로 수정했다.

- [Nginx 내부 접근 로그](./docs/logs/docker/docker_practice/docker_exec%20-it)
- [Nginx 실행 로그](./docs/logs/docker/docker_practice/docker_nginx.txt)

---

## 13. Docker 로그 확인

```bash
docker logs <컨테이너_ID>
docker logs --tail 10 <컨테이너_ID>
docker logs -f <컨테이너_ID>
docker logs --tail 0 -f <컨테이너_ID>
```

| 명령 | 의미 |
|---|---|
| `docker logs` | 지금까지 출력된 로그 전체 확인 |
| `--tail 10` | 마지막 10줄만 확인 |
| `-f` | 새 로그를 실시간으로 계속 확인 |
| `--tail 0 -f` | 기존 로그를 제외하고 새 로그부터 확인 |

- [Docker 로그 확인 실습](./docs/logs/docker/docker_practice/docker_logs)

---

## 14. 포트 매핑

```bash
docker run -d -p 4000:80 nginx
docker ps
```

`-p 4000:80`은 호스트의 4000번 포트를 컨테이너의 80번 포트에 연결한다.

```text
브라우저 또는 호스트 :4000 → 컨테이너 Nginx :80
```

컨테이너는 독립된 네트워크 환경에서 실행되므로 호스트에서 접근하려면 포트 연결이 필요하다.

- [포트 매핑 확인 로그](./docs/logs/docker/docker_practice/docker_mapping)
- [포트 매핑 확인 로그](./docs/images/conect.png)
> 현재 로그는 포트 매핑 상태까지만 증명한다. 실제 HTTP 접속 성공을 증명하려면 `curl -i http://localhost:4000`의 출력 또는 브라우저 화면을 추가해야 한다.

---

## 15. MySQL 데이터 영속성 확인(바인드 마운트)

### 15.1 마운트하지 않은 경우

MySQL 컨테이너 안에서 `mydb` 데이터베이스를 생성한 뒤 컨테이너를 삭제하고 새 컨테이너를 만들었다.

```sql
CREATE DATABASE mydb;
SHOW DATABASES;
```

새 컨테이너에서는 `mydb`가 보이지 않았다. 별도의 저장 공간을 연결하지 않으면 데이터가 컨테이너의 쓰기 계층에 저장되므로 컨테이너 삭제와 함께 사라진다.

- [마운트하지 않은 MySQL 실습](./docs/logs/docker/docker_practice/docker_volume_Non)

### 15.2 바인드 마운트를 사용한 경우

```bash
docker run \
  --name mysql-practice \
  -e MYSQL_ROOT_PASSWORD='[비밀번호]' \
  -d \
  -p 3306:3306 \
  -v "$HOME/downloads/docker:/var/lib/mysql" \
  mysql
```

호스트의 `$HOME/downloads/docker` 폴더와 컨테이너의 `/var/lib/mysql`을 연결했다. 첫 번째 컨테이너에서 `mydb`를 생성한 뒤 컨테이너를 삭제하고, 같은 호스트 폴더를 연결한 새 MySQL 컨테이너를 실행했다. 새 컨테이너에서 `SHOW DATABASES;`를 실행했을 때 `mydb`가 다시 출력되는 결과를 확인했다. 다만 기존 원본 기록에는 첫 번째 컨테이너 삭제 명령이 빠져 있으므로, 평가용 완전한 증거를 위해 삭제와 재생성을 연속으로 기록한 로그를 추가해야 한다.

```text
첫 번째 컨테이너: mydb 생성
→ 첫 번째 컨테이너 삭제
→ 같은 바인드 마운트로 새 컨테이너 생성
→ 새 컨테이너에서 mydb 확인 성공
```

- [바인드 마운트 MySQL 실습](./docs/logs/docker/docker_practice/docker_volume)

> 이 명령의 `-v` 왼쪽 값은 호스트 경로이므로 **바인드 마운트**다. Docker가 관리하는 이름 있는 볼륨을 사용하려면 `-v codyssey-data:/var/lib/mysql`처럼 왼쪽에 볼륨 이름을 작성해야 한다.

---

## 16. 바인드 마운트와 Docker 볼륨 비교

| 구분 | 바인드 마운트 | Docker 볼륨 |
|---|---|---|
| 왼쪽 값 예시 | `$HOME/downloads/docker` | `codyssey-data` |
| 저장 위치 | 사용자가 지정한 호스트 경로 | Docker가 관리하는 영역 |
| 경로 의존성 | 호스트 경로에 의존 | 상대적으로 낮음 |
| 주요 용도 | 개발 소스·설정 파일 연결 | 데이터베이스·서비스 데이터 보존 |

- **Bind Mount**: 컨테이너 밖에 있는 내 Mac의 특정 폴더 경로를 직접 지정하여 데이터를 남기는 방식
- **Docker Volume**: 컨테이너 밖에 Docker가 관리하는 전용 저장 공간을 할당하여 데이터를 남기는 방식

**참고 영상**

- [Docker Bind Mount와 Volume 참고 영상](https://www.youtube.com/watch?v=OPmSQCfzl1Q&list=PLtUgHNmvcs6rS5aNCRIZtVcyk3gRX2iOd)

현재 완료한 MySQL 실습은 바인드 마운트이다. 이름 있는 Docker 볼륨 실습은 다음 명령으로 추가 검증할 수 있다.

```bash
docker volume create codyssey-data

docker run -d \
  --name mysql-volume-test \
  -e MYSQL_ROOT_PASSWORD='[비밀번호]' \
  -v codyssey-data:/var/lib/mysql \
  mysql

docker volume ls
docker volume inspect codyssey-data
```

---

## 17. Git과 GitHub 연동

### 17.1 역할 차이

- **Git**: 내 컴퓨터에서 파일 변경 이력과 커밋을 관리하는 도구
- **GitHub**: Git 저장소를 온라인에 보관하고 공유·협업하는 서비스

```bash
git --version
git config --global --get user.name
git config --global --get user.email
git config --global --get init.defaultBranch
git branch --show-current
git remote -v
```

기본 브랜치가 `main`이고 원격 저장소가 `Kfri-cloud/Codyssey`를 가리키는 것을 확인했다. 공개 문서에서는 이메일 주소를 마스킹했다.

![Git 설정 확인](./docs/images/11-git-config.png)

![GitHub 원격 저장소 확인](./docs/images/12-github-remote.png)

- [실제 GitHub push 및 원격 커밋 근거](./docs/logs/git/push_evidence.md)

---

## 18. 트러블슈팅

### 18.1 명령과 옵션 사이의 공백 누락

**문제**

```text
exec: "ls-la": executable file not found in $PATH
```

**원인**

`ls-la`를 하나의 실행 파일 이름으로 해석했지만 해당 파일이 존재하지 않았다.

**확인 및 해결**

```bash
docker exec ubuntu-practice00 ls -la /
```

`ls`와 `-la` 사이에 공백을 넣어 정상적으로 파일 목록을 확인했다.

![옵션 공백 오류](./docs/images/10-background-name-error.png)

### 18.2 MySQL 명령 실행 위치 오류

**문제**

컨테이너의 Bash에서 바로 `show databases;`를 입력하자 다음 오류가 발생했다.

```text
bash: show: command not found
```

**원인**

`SHOW DATABASES;`는 Bash 명령이 아니라 MySQL 클라이언트 안에서 사용하는 SQL 문이다.

**해결**

```bash
mysql -u root -p
```

MySQL에 접속한 뒤 `SHOW DATABASES;`를 실행해 정상적으로 데이터베이스 목록을 확인했다.

### 18.3 실행 중인 컨테이너 삭제 오류

**문제**

```text
container is running: stop the container before removing or force remove
```

**원인**

`docker rm`은 기본적으로 실행 중인 컨테이너를 삭제하지 않는다.

**해결**

```bash
docker stop <컨테이너_ID>
docker rm <컨테이너_ID>
```

또는 실습 컨테이너임을 확인한 뒤 다음 명령으로 강제 정리했다.

```bash
docker rm -f <컨테이너_ID>
```

---

## 19. 보안 및 개인정보 보호

- GitHub에는 실제 비밀번호, 토큰, 개인키, 인증 코드를 올리지 않는다.
- README의 MySQL 비밀번호는 `[비밀번호]`로 마스킹한다.
- 터미널 캡처에서는 사용자명과 이메일을 가린다.
- `.DS_Store`는 프로젝트 파일이 아니므로 `.gitignore`에 추가한다.
- 이미 공개 저장소에 실제 비밀번호를 올렸다면 파일만 수정하지 말고 해당 비밀번호도 변경한다.

권장 `.gitignore`:

```gitignore
.DS_Store
.env
*.pem
*.key
```

---

## 20. 결과 요약

이번 실습을 통해 터미널 기본 조작, Docker Client와 Server의 관계, 이미지와 컨테이너의 차이, 컨테이너의 생성·실행·중지·삭제 흐름을 확인했다.

또한 Nginx 컨테이너 내부에 접속해 설정 파일을 살펴보고, 로그 확인과 포트 매핑을 실습했다. MySQL 실습에서는 저장 공간을 연결하지 않으면 컨테이너 삭제 시 데이터가 사라지고, 호스트 디렉터리를 바인드 마운트하면 새 컨테이너에서도 데이터가 유지되는 차이를 확인했다.

현재 실제 증거가 남아 있는 항목만 완료로 표시했다. `hello-world` 실행과 원격 GitHub 커밋은 별도 로그로 보강했다. MySQL 재연결 후 `mydb`가 조회된 결과는 있으나 삭제 명령을 포함한 연속 로그가 필요하며, 포트 매핑도 실제 HTTP 응답 증거를 추가해야 한다. Dockerfile 빌드, 이름 있는 볼륨, 파일 권한 변경 결과 역시 실제 실행 로그가 확인되면 완료 처리한다.


---

## 21. 동작 구조 설계 설명

### 21.1 프로젝트 디렉터리 구성 기준

프로젝트 루트인 `E1-1` 아래에서 문서와 증거 자료를 역할별로 분리했다.

- `README.md`: 전체 실습 목적, 명령, 결과와 해석
- `docs/images`: 화면으로 확인해야 하는 실행 증거
- `docs/logs`: 명령과 전체 출력 원문
- `docs/logs/docker/docker_practice`: Docker 세부 실습별 로그

이 구조를 사용하면 README는 설명 중심으로 읽고, 자세한 근거가 필요할 때 연결된 이미지와 로그를 열어 확인할 수 있다.

### 21.2 포트와 저장 공간의 재현 방법

포트 매핑은 항상 `호스트 포트:컨테이너 포트` 순서로 기록했다.

```bash
docker run -d -p 4000:80 nginx
```

```text
호스트 4000번 포트 → 컨테이너 Nginx 80번 포트
```

MySQL 저장 공간은 `호스트 경로:컨테이너 경로`로 기록했다.

```bash
-v "$HOME/downloads/docker:/var/lib/mysql"
```

다른 컴퓨터에서 재현할 때는 `$HOME/downloads/docker` 부분만 해당 컴퓨터의 저장 경로로 바꾸면 된다.

---

## 22. 핵심 기술 원리

### 22.1 이미지와 컨테이너: 빌드·실행·변경 관점

| 관점 | 이미지 | 컨테이너 |
|---|---|---|
| 빌드 | Dockerfile 또는 기존 이미지를 통해 생성되는 읽기 전용 결과물 | 직접 빌드하지 않고 이미지로부터 생성 |
| 실행 | 그 자체로 실행되는 프로세스가 아님 | 이미지의 명령을 실제 프로세스로 실행 |
| 변경 | 같은 태그를 다시 빌드하면 새로운 이미지가 만들어질 수 있음 | 실행 중 생성된 파일은 컨테이너 쓰기 계층에 저장 |
| 삭제 영향 | 이미지를 삭제해도 이미 생성된 컨테이너와는 생명주기가 구분됨 | 저장 공간을 연결하지 않으면 삭제 시 내부 변경 데이터도 사라짐 |

쉽게 말하면 이미지는 실행 환경의 설계도이고, 컨테이너는 그 설계도로 실제 가동한 작업 공간이다.

### 22.2 컨테이너 내부 포트에 직접 접속할 수 없는 이유

컨테이너는 호스트와 분리된 네트워크 공간을 사용한다. Nginx가 컨테이너 내부 80번 포트에서 실행되어도 호스트의 80번 또는 4000번 포트와 자동으로 연결되지 않는다.

```bash
docker run -d -p 4000:80 nginx
```

따라서 `-p`로 호스트가 받을 포트와 컨테이너 서비스 포트를 연결해야 브라우저나 `curl`에서 접근할 수 있다.

### 22.3 절대 경로와 상대 경로 선택 기준

- 절대 경로는 실행 위치와 관계없이 항상 같은 파일을 지정해야 할 때 사용한다.
- 상대 경로는 프로젝트 내부 파일처럼 저장소를 다른 위치로 옮겨도 관계를 유지해야 할 때 사용한다.
- README 이미지와 로그에는 저장소 이동 가능성을 위해 상대 경로를 사용했다.
- 호스트 폴더를 컨테이너에 연결할 때는 Docker가 정확한 위치를 찾을 수 있도록 `$HOME`에서 확장되는 경로를 사용했다.

### 22.4 숫자 권한 결정 규칙

각 사용자 범위에서 읽기 4, 쓰기 2, 실행 1을 더한다.

```text
7 = 4 + 2 + 1 = rwx
6 = 4 + 2     = rw-
5 = 4 + 1     = r-x
4 = 4         = r--
```

세 자리 숫자는 소유자, 그룹, 기타 사용자 순서다.

```text
755 = 소유자 rwx / 그룹 r-x / 기타 r-x
644 = 소유자 rw- / 그룹 r-- / 기타 r--
```

일반적인 디렉터리는 내부 접근을 위해 `x`가 필요한 경우가 많아 `755`, 일반 문서 파일은 실행할 필요가 없어 `644`를 사용한다.

---

## 23. 심층 인터뷰 대비

### 23.1 호스트 포트가 이미 사용 중일 때 진단 순서

1. Docker 오류에서 충돌한 포트 번호를 확인한다.
2. 실행 중인 컨테이너가 그 포트를 사용하는지 확인한다.

```bash
docker ps
```

3. macOS에서 어떤 프로세스가 포트를 점유하는지 확인한다.

```bash
lsof -i :4000
```

4. 불필요한 컨테이너나 프로세스라면 안전하게 중지한다.

```bash
docker stop <컨테이너_ID>
```

5. 종료하면 안 되는 서비스라면 호스트 포트만 다른 번호로 변경한다.

```bash
docker run -d -p 4001:80 nginx
```

6. `docker ps`와 `curl`로 최종 연결을 검증한다.

```bash
docker ps
curl http://localhost:4001
```

### 23.2 컨테이너 삭제 후 데이터가 사라지는 것을 막는 방법

컨테이너 내부 쓰기 계층에만 저장된 데이터는 컨테이너 삭제 시 함께 사라진다. 이를 막으려면 다음 방법을 사용한다.

- 개발 파일처럼 호스트에서 직접 관리할 자료: 바인드 마운트
- 데이터베이스처럼 Docker가 독립적으로 관리할 자료: 이름 있는 Docker 볼륨
- 외부 서비스가 관리해야 하는 자료: 외부 데이터베이스나 오브젝트 스토리지

이번 실습에서는 MySQL의 `/var/lib/mysql`을 호스트 디렉터리에 바인드 마운트했다. 첫 번째 컨테이너를 삭제하고 새 컨테이너에 같은 경로를 연결했을 때 `mydb`가 남아 있어 데이터 영속성을 확인했다.

### 23.3 가장 어려웠던 지점과 해결 과정

가장 혼동된 지점은 MySQL 명령을 어느 환경에서 입력해야 하는지와, 컨테이너 삭제 후 데이터를 어떻게 보존하는지였다.

**가설**

`SHOW DATABASES;`를 컨테이너 Bash에서 바로 실행할 수 있고, 컨테이너가 바뀌어도 데이터가 자동으로 유지될 것으로 생각했다.

**확인**

Bash에서 `show databases;`를 입력하자 다음 오류가 발생했다.

```text
bash: show: command not found
```

또한 저장 공간을 연결하지 않은 컨테이너를 삭제하고 새 MySQL 컨테이너를 만들었을 때 `mydb`가 사라진 것을 확인했다.

**조치**

`mysql -u root -p`로 MySQL 클라이언트에 들어간 뒤 SQL을 실행했다. 이후 호스트 디렉터리를 `/var/lib/mysql`에 연결하고 컨테이너를 재생성했다.

**결과**

새 컨테이너에서 `SHOW DATABASES;`를 실행했을 때 `mydb`가 다시 출력됐다. 이를 통해 Bash 명령과 SQL 명령의 실행 위치, 컨테이너 쓰기 계층과 외부 저장 공간의 차이를 확인했다.
