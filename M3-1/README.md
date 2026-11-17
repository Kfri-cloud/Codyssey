# M3-1 | 내가 만든 웹사이트를 인터넷에 올려 누구나 쓰게 하기

> Codyssey Basic Cloud & AI API · AWS 실습 평가 및 증빙 템플릿
>
> **상태: 제출 양식 준비 완료 / 실제 AWS 구축·외부 접속·삭제 검증은 미실시.** 문서의 `[입력]`, `[ ]`는 실제 결과로 채워야 합니다.

## 제출물 (원문 3-1.pdf 2쪽)

| 구분 | 파일 | 필수 증빙 |
|---|---|---|
| 1. 아키텍처 | [docs/architecture.md](docs/architecture.md), [docs/architecture.svg](docs/architecture.svg) | VPC, Public Subnet, IGW, Route Table, EC2, SG 및 외부 요청 흐름; 최종 PNG/PDF로 내보내기 |
| 2. 외부 접속 | 아래 '접속 검증' + `docs/evidence/` 스크린샷 | 방식 A/B 중 하나와 외부 응답 |
| 3. 트러블슈팅 | [docs/troubleshooting.md](docs/troubleshooting.md) | 실제 오류 1건 이상: 증상→가설→검증→조치→결과→재발 방지 |
| 4. 정리 | [docs/cleanup-checklist.md](docs/cleanup-checklist.md) | EC2/EBS/EIP/IGW/VPC 최소 5종 및 추가 요금 리소스 |

## 실습 환경 / 구성 기록

| 항목 | 실제 사용값 |
|---|---|
| AWS Region | ap-northeast-2 (서울) |
| VPC CIDR / 이름 | [입력] |
| Public Subnet CIDR / AZ | [입력] |
| Internet Gateway ID | [입력] |
| Public Route Table ID | [입력] |
| EC2 / AMI / 인스턴스 유형 | [입력] |
| 퍼블릭 IPv4 또는 DNS | [입력 — 삭제 후 접속 불가] |
| 웹 서버 | [Nginx 등 입력] |
| SG 이름 / ID | [입력] |
| IAM 주체 / 부여 정책 | [입력 — 비밀·계정 ID 불필요] |
| 리소스 추적 태그 | Project=codyssey-m3-1, Owner=[별칭], Environment=lab |

**보안:** 퍼블릭 IP, 이름, SG 규칙은 공개해도 되는 범위만 기록합니다. AWS 액세스 키, 비밀 키, SSH 개인키(PEM), 계정 번호, 민감 로그는 Git에 절대 올리지 마세요. 공개 저장소의 캡처는 마스킹 후 사용하세요.

## 실행/설정 체크리스트 (항목 1)

- [ ] VPC 1개, Public Subnet 1개 생성
- [ ] IGW를 VPC에 연결
- [ ] Public Subnet이 연동된 Route Table에 `0.0.0.0/0 → IGW` 등록
- [ ] Public Subnet의 EC2에 퍼블릭 IPv4 할당, SSH 접속 성공
- [ ] 웹 서버 실행, EC2 안에서 `curl -i http://localhost/` 응답 200 확인
- [ ] SG 인바운드: TCP 80 = `0.0.0.0/0`, TCP 22 = **내 공인 IP/32만**. 그 외 불필요한 인바운드 미허용
- [ ] IAM은 EC2/VPC/SG 등의 실습 필요 작업으로만 제한하며 AdministratorAccess 사용 안 함
- [ ] 외부 검증 A/B 중 하나 성공, 실제 스크린샷 및 URL/IP 기록
- [ ] 트러블슈팅 실제 1건 이상 기록
- [ ] 종료 후 리소스 정리 증빙 (최소 5종) 완료

## 서버 배포 및 테스트 예시 (Ubuntu + Nginx)

```bash
# 1. (로컬 컴퓨터) 본인 키 경로, 퍼블릭 IP로 변경
chmod 400 /path/to/lab-key.pem
ssh -i /path/to/lab-key.pem ubuntu@<PUBLIC_IP>

# 2. (EC2 내부) 패키지 설치 및 시작
sudo apt update
sudo apt install -y nginx
sudo systemctl enable --now nginx
sudo systemctl status nginx --no-pager

# 3. (EC2 내부) localhost 응답 확인
curl -i http://localhost/
```

Amazon Linux이면 패키지 관리 명령, SSH 사용자(`ec2-user`)가 달라집니다. 로컬의 SSH `chmod`는 Windows PowerShell에는 그대로 적용되지 않을 수 있습니다.

## 외부 접속 검증 — **A 선택(권장·간단)**

- 방식: **A. 브라우저 http://<PUBLIC_IP> 접속 후 페이지 표시**
- 실제 사용 URL: `http://[실제 퍼블릭 IP]/`
- 검증 시각(KST): [입력]
- 결과: [미검증 / 성공 / 실패]
- 증빙: `docs/evidence/external-browser.png` [추가 필요]
- 브라우저에서 나온 화면과 주소창(필요 시 일부 마스킹)을 캡처합니다.

대체 방식 B: `curl -i http://<PUBLIC_IP>/health`에서 HTTP 200 및 고정 문구 `OK`를 **실제로 서버에 /health 경로를 구현한 뒤** 검증. Nginx 기본 설치만으로는 `/health`가 자동 제공되지 않습니다.

## 평가 설명 자료

문답 및 상황 대처: [docs/evaluation-guide.md](docs/evaluation-guide.md).

## 최종 제출 전 확인

1. `docs/architecture.svg`를 실제 구성과 맞게 수정하고 **PNG 또는 PDF 1장**으로 내보내 `docs/architecture.png` 또는 `docs/architecture.pdf` 추가
2. 브라우저 증빙을 `docs/evidence/external-browser.png`에 추가
3. 트러블슈팅을 가상 예제가 아닌 **실제 사건**으로 변경
4. 정리 체크리스트를 AWS 콘솔에서 확인하고 체크
5. 작업 완료 후 비용 대시보드 확인 (표시 지연 가능)

> 템플릿은 평가 대비 자료이지, AWS에 리소스를 실제로 생성하거나 결과를 검증한 기록이 아닙니다.
