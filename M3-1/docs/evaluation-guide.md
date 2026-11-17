# 미션 3-1 평가 대비 문답 (항목 2·3·4)

## 항목 2 — 구현 설명

**Q. 외부 → IGW → Subnet → EC2 흐름은?**  
A. 브라우저가 퍼블릭 IPv4로 HTTP(80) 요청 → 인터넷/IGW → 퍼블릭 서브넷의 EC2 → 보안 그룹 허용 확인 → Nginx 응답. Public Route Table은 `0.0.0.0/0 → IGW`여야 하며 SG·퍼블릭 IP·프로세스 구동도 확인합니다.

**Q. SG는 어떻게 최소화했나요?**  
A. HTTP 80만 전체 인터넷에 공개하고 SSH 22는 실제 관리자의 공인 IP/32에만 열었습니다. DB 3306/5432, 불필요한 관리 포트 및 전체 범위 개방은 허용하지 않았습니다. (실제 규칙이 같을 때만 이 답변을 사용)

**Q. 외부 검증은 A/B 중 무엇이고 어떻게 구성했나요?**  
A. 예시 선택은 **A (브라우저)** 입니다. EC2 Nginx 설치/시작 → `curl -i http://localhost/` 확인 → 인스턴스에 퍼블릭 IP와 SG 80 허용 확인 → 외부 브라우저 `http://<PUBLIC_IP>` 테스트 → 화면 캡처. 실습 후 결과로 교체하세요.

**Q. 리소스를 어떻게 추적/정리했나요?**  
A. 예시 태그는 `Project=codyssey-m3-1`, `Owner=별칭`, `Environment=lab`. EC2, EBS, EIP, IGW, VPC 및 종속 리소스를 체크리스트로 추적하고 종료 시 확인합니다.

## 항목 3 — 설계 이유

**Q. Public Route Table 기본 경로가 필요한 이유는?**  
A. VPC 내부 경로 외 목적지로 통신할 때 인터넷 게이트웨이로 보내기 위해서입니다. 서브넷 연결(association)과 인스턴스 퍼블릭 IP도 함께 필요합니다.

**Q. Security Group과 IAM의 책임 차이는?**  
A. **SG**는 인스턴스 ENI 수준의 네트워크 트래픽(허용 포트/소스) 제어, **IAM**은 AWS API와 리소스 작업을 수행할 수 있는 자격 주체의 권한 제어입니다. 최소 권한으로 유출·오작동 시 피해 범위를 줄입니다.

**Q. SSH(22)나 DB 포트를 0.0.0.0/0로 열면 왜 안 되나요?**  
A. 누구나 접속 시도를 할 수 있어 공격 노출이 커집니다. SSH는 공인 IP/32 제한 또는 SSM Session Manager(구성 가능할 때)로 관리하고, DB는 프라이빗 서브넷/필요한 SG 간 통신만 허용합니다.

**Q. 가설→검증 순서를 지키는 이유는?**  
A. 무작정 설정을 바꾸면 원인 분리가 어렵고 보안을 약화할 수 있기 때문입니다. 상태 코드, `curl`, `systemctl`, `journalctl`, SG/라우팅 확인 결과를 기록해 가설을 반증하거나 지지한 뒤 한 번에 한 설정씩 수정합니다.

## 항목 4 — 문제 해결·확장

**Q. 외부 접속 안 되면 어떤 순서로?**  
A. ① Route Table 기본 경로/서브넷 연결/IGW 연결 확인 ② SG(필요시 NACL) 확인 ③ EC2 퍼블릭 IP/DNS 상태 확인 ④ EC2 내부 `systemctl status nginx`, `ss -lntp`, `curl -i localhost`, `journalctl -u nginx` 확인. 각 단계 결과를 적습니다.

**Q. IAM 권한 부족 시?**  
A. 실패한 API 작업명과 `AccessDenied`의 주체·리소스를 확인하고 CloudTrail/정책 시뮬레이터·IAM 오류 세부정보로 필요한 Action/Resource/Condition을 좁힙니다. 제한된 정책 변경을 요청하며 AdministratorAccess를 무작정 붙이지 않습니다.

**Q. EC2 2대로 확장한다면?**  
A. 단일 EC2의 CPU/메모리 및 장애 시 중단이 병목/단일 장애점입니다. 동일 웹 서버 2대(가급적 다른 AZ의 서브넷)와 **ALB + Target Group + Health Check**, 필요하면 Auto Scaling을 추가합니다. 인스턴스 SG는 ALB SG에서만 웹 트래픽 허용하고, ALB는 외부 80/443을 처리하도록 설계합니다.

**Q. Billing 비용이 예상보다 나오면?**  
A. Billing/Cost Explorer에서 리전·서비스·사용량을 나누고, EBS 미연결 볼륨/스냅샷, Elastic IP/공용 IPv4, EC2 실행 인스턴스, NAT Gateway, ALB, RDS부터 확인합니다. 실습 태그와 리소스 목록으로 추적하고 의존 순서대로 정리한 뒤 Billing을 다시 확인합니다. 비용 데이터 반영은 지연될 수 있습니다.

## 발표용 30초 요약

“서울 리전에서 VPC와 퍼블릭 서브넷을 생성하고 IGW와 기본 경로를 연결했습니다. EC2에 웹 서버를 구동하고 인바운드 HTTP 80만 공개, SSH 22는 제 IP로 제한하도록 설계했습니다. 브라우저 외부 접속을 검증하고 문제 발생 시 라우팅, 보안 그룹, IP, 서비스 로그 순서로 원인을 조사합니다. 종료 후 EC2·EBS·EIP·IGW·VPC를 확인해 비용 발생을 방지합니다.”

*위 요약은 완료 후에만 과거형으로 발표하세요. 현재는 평가 대비 예시입니다.*
