# Git 공부 가이드

Git 명령어를 효과적으로 학습하고 사용하는 방법을 정리한 문서입니다. 이 문서는 학습한 내용을 깔끔하게 정리하고 실습 예제를 포함하여 구성되었습니다.

---

## 목차

1. [Git 기본 개념](#git-기본-개념)
2. [`.gitignore` 활용](#gitignore-활용)
3. [Git 명령어](#git-명령어)
    - [Revert](#git-revert)
    - [Reset](#git-reset)
4. [TIL (Today I Learned)](#til-today-i-learned)
5. [심화 개념](#심화-개념)
    - [API 기본](#api-기본)

---

## Git 기본 개념

- Git은 코드 변경 사항을 관리할 수 있는 버전 관리 시스템입니다.
- `git init`, `git status`, `git add`와 같은 명령어는 Git 저장소를 초기화하고 파일을 관리하는 기본 명령어입니다.

### 주요 Git 명령어

| 명령어                      | 설명                                              |
|-----------------------------|---------------------------------------------------|
| `git init`                  | 새 Git 저장소를 초기화합니다.                     |
| `git status`                | 현재 저장소 상태를 확인합니다.                    |
| `git add <파일>`            | 파일을 스테이징 영역에 추가합니다.                 |
| `git commit -m "메시지"`   | 스테이징된 변경 사항을 커밋합니다.                |

---

## `.gitignore` 활용

- `.gitignore` 파일은 Git이 특정 파일과 디렉토리를 무시하도록 설정합니다.
- 민감 정보나 불필요한 파일(예: 로그 파일, 시스템 파일 등)을 추적하지 않도록 도와줍니다.

### 주요 포인트

1. Git이 이미 추적 중인 파일은 `.gitignore`에 추가하더라도 무시되지 않습니다. 이 경우 아래 명령어로 캐시에서 제거해야 합니다:
   ```bash
   git rm --cached <파일>
   ```

2. [gitignore.io](https://www.toptal.com/developers/gitignore/) 같은 툴을 사용하면 프로젝트에 맞는 `.gitignore` 파일을 쉽게 생성할 수 있습니다.

### 예제 워크플로우
```bash
$ touch .gitignore
$ echo "*.log" >> .gitignore  # 모든 .log 파일 무시
$ git add .gitignore
$ git commit -m "Add .gitignore file"
```

---

## Git 명령어

### Git Revert

- `git revert`는 특정 커밋의 변경 사항을 취소하는 새 커밋을 생성합니다.
- **히스토리를 안전하게 유지**하며 변경 사항을 취소할 수 있는 방법입니다.

#### 예제:
```bash
$ git log --oneline
f7b3a3d 첫 번째 커밋
91cb4a2 두 번째 커밋
$ git revert 91cb4a2
[master a178ae1] Revert "두 번째 커밋"
```

### Git Reset

- `git reset`은 HEAD를 특정 커밋으로 이동시키며, 옵션에 따라 스테이징 영역이나 작업 디렉토리에 영향을 줄 수 있습니다.

#### Reset 옵션

| 옵션       | 설명                                           |
|------------|------------------------------------------------|
| `--soft`   | HEAD만 이동하고 변경 사항을 스테이징 상태로 유지.|
| `--mixed`  | HEAD를 이동하고 변경 사항을 스테이징 해제.       |
| `--hard`   | HEAD를 이동하고 모든 변경 사항을 삭제.          |

#### 예제:
```bash
$ git log --oneline
f7b3a3d 첫 번째 커밋
91cb4a2 두 번째 커밋
$ git reset --hard f7b3a3d
HEAD가 f7b3a3d로 이동했습니다.
```

---

## TIL (Today I Learned)

- 학습한 내용을 기록하고 정리하여 활용도를 높입니다.
- 단순 이론 기록에 그치지 말고, 이를 실무에 적용하거나 문제 해결에 사용한 사례를 포함하세요.

#### 예제 형식:
```markdown
### 학습 내용
- **Git 기본**: `git status`를 사용하여 작업 디렉토리 상태를 확인.
- **활용 사례**: `.gitignore` 파일을 만들어 불필요한 파일을 제외.
```

---

## 심화 개념

### API 기본

- API(Application Programming Interface)는 서로 다른 소프트웨어가 통신할 수 있도록 돕는 인터페이스입니다.
- 예: 날씨 API를 이용해 실시간 데이터를 가져오기.

#### 주요 용어

| 용어         | 설명                                           |
|--------------|------------------------------------------------|
| **클라이언트**| 요청을 보내는 주체 (예: 브라우저, 앱).          |
| **서버**      | 요청을 처리하고 응답을 보내는 주체.            |
| **API 키**    | 인증을 위해 사용하는 고유 키.                  |

#### 예제:
```python
import requests

API_KEY = "your_api_key"
url = f"https://api.example.com/data?key={API_KEY}"
response = requests.get(url)
print(response.json())
```

---

### 참고 자료

1. [Git 공식 문서](https://git-scm.com/doc)
2. [GitHub 가이드](https://guides.github.com/)
3. [Markdown 가이드](https://www.markdownguide.org/)

---


