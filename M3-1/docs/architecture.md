# 네트워크 아키텍처 — 구성 설명 및 다이어그램

![구성도](architecture.svg)

**참고 구성(실제 값 아님):** Region `ap-northeast-2`; VPC `10.0.0.0/16`; Public Subnet `10.0.1.0/24`. 생성 후 CIDR/리소스 ID/보안 그룹 규칙을 실제 값으로 수정합니다.

```mermaid
flowchart TB
  U["외부 사용자 · 브라우저 HTTP 80"]
  I["Internet"]
  G["Internet Gateway (VPC 연결)"]
  subgraph V["VPC · 예시 10.0.0.0/16"]
    R["Public Route Table\n0.0.0.0/0 → IGW"]
    subgraph S["Public Subnet · 예시 10.0.1.0/24"]
      SG["Security Group\n80 ← 0.0.0.0/0\n22 ← 내 IP/32"]
      E["EC2 · 퍼블릭 IPv4 · Nginx :80"]
      SG --> E
    end
    R -. "서브넷 연결" .-> S
  end
  U --> I --> G --> SG
  G -. "VPC 인터넷 경로" .-> R
```

## 외부 요청 흐름 (항목 2)

1. 외부 브라우저가 EC2의 퍼블릭 IPv4:80으로 요청합니다.
2. 트래픽은 인터넷과 **VPC에 연결된 IGW**를 거쳐 대상 EC2의 네트워크 인터페이스로 전달됩니다.
3. Public Subnet의 연결된 Route Table은 기본 경로 `0.0.0.0/0 → IGW`를 가져 인터넷 송수신 경로를 구성합니다. 이 규칙이 없으면 일반적인 IPv4 인터넷 접속 경로가 성립하지 않습니다.
4. 보안 그룹 인바운드가 TCP 80 요청을 허용하고 EC2의 Nginx가 처리해 응답합니다. 응답은 상태 저장형 SG의 반환 트래픽 허용을 이용해 클라이언트로 돌아갑니다.
5. SSH 관리는 TCP 22를 특정 관리자 IP/32에만 허용합니다.

**정확성 유의:** Route Table의 0.0.0.0/0은 주로 인스턴스에서 인터넷으로 나가는 경로를 지정하고, IGW가 외부와의 양방향 연결을 지원합니다. 퍼블릭 IPv4, SG, Network ACL, 인스턴스 리스닝 상태도 외부 접근 조건입니다. IGW가 SG를 순서대로 '통과'하는 물리적 상자가 아니라 논리적으로 서로 다른 제어 요소임을 설명하세요.

## 설계 검증 자료

| 확인 항목 | 콘솔 위치 | 증빙 |
|---|---|---|
| VPC CIDR | VPC → Your VPCs | [캡처/값] |
| Subnet CIDR/공개 여부 | VPC → Subnets | [캡처/값] |
| IGW 연결 | VPC → Internet Gateways | [캡처/값] |
| 0.0.0.0/0 기본 경로 및 연결 | VPC → Route Tables → Routes / Subnet associations | [캡처/값] |
| EC2 퍼블릭 IPv4 | EC2 → Instances → Networking | [캡처/값] |
| SG TCP 80 / SSH 22 소스 | EC2 → Security Groups → Inbound rules | [캡처/값] |

원문 제출 파일 형식은 **PNG 또는 PDF 1장**입니다. 이 SVG는 편집용 시각 자료이므로 실제 구성 반영 후 PNG/PDF로 내보내 제출하세요.
