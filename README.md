# Python 기반 데이터 분석 및 데이터 시각화를 위한 Streamlit 웹 대시보드

## 과정 소개
본 저장소는  
「Python 기반 데이터 분석 및 데이터 시각화를 위한 Streamlit 웹 대시보드」강의 학습 내용을 정리하기 위한 저장소입니다.

Python을 활용한 데이터 분석 및 시각화 과정과 Streamlit 기반 웹 대시보드 구현 내용을 학습 및 실습 중심으로 기록합니다.

---

## 학습 목표
- Python 데이터 분석 기초 학습
- Pandas 기반 데이터 처리 및 전처리
- 데이터 시각화 구현
- Streamlit 기반 웹 대시보드 개발
- 데이터 기반 인사이트 도출
- Git & GitHub 기반 학습 관리

---

## 학습 기술 스택

<details>
<summary>Language</summary>

### Python

* 기본 문법
* 함수
* 리스트 · 딕셔너리
* 반복문 · 조건문
* 파일 입출력

</details>

<details>
<summary>Data Analysis</summary>

### NumPy

* ndarray
* 벡터 연산
* 배열 인덱싱
* shape / dtype / ndim

### Pandas

* DataFrame 탐색
* 결측치 처리
* groupby / agg
* 데이터 전처리
* 시계열 데이터 처리

</details>

<details>
<summary>Machine Learning</summary>

### scikit-learn

* 머신러닝 파이프라인
* 모델 학습 · 예측 · 평가

#### Classification
- KNeighborsClassifier
- Logistic Regression
- SGDClassifier
- DecisionTreeClassifier
- RandomForestClassifier
- GradientBoostingClassifier

#### Regression
- Linear Regression
- KNeighborsRegressor
- Ridge
- Lasso

#### Ensemble Learning
- Random Forest
- Gradient Boosting
- HistGradientBoosting
- XGBoost
- LightGBM

</details>

<details>
<summary>Data Preprocessing</summary>

### Preprocessing

* StandardScaler
* PolynomialFeatures
* train_test_split
* Data Leakage 방지
* One-Hot Encoding

</details>

<details>
<summary>Evaluation Metrics</summary>

### Classification Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

### Regression Metrics

* R²
* MAE
* MSE

</details>

<details>
<summary>Visualization</summary>

### Matplotlib

* scatter plot
* line plot
* histogram
* regression line
* learning curve

### Plotly

* interactive chart
* dashboard visualization
* ROC visualization

### Seaborn

* heatmap
* confusion matrix visualization

</details>

<details>
<summary>Dashboard</summary>

### Streamlit

* interactive dashboard
* sidebar filtering
* metric visualization
* plotly integration

</details>

<details>
<summary>Development Environment</summary>

### VS Code

* Python 개발 환경
* Git 연동

### Jupyter Notebook

* 데이터 분석 실습
* 머신러닝 실험
* 시각화 실습

</details>

<details>
<summary>Version Control</summary>

### Git

* branch 관리
* commit 관리
* 원격 저장소 연동

### GitHub

* repository 관리
* README 작성
* 프로젝트 버전 관리

</details>

---

## 학습 내용

<details>
<summary>2026-05-18 | CLI & Git 기초</summary>

### CLI 명령어
```bash
pwd          # 현재 위치 확인
cd           # 폴더 이동
mkdir        # 폴더 생성
ls           # 파일 목록 확인
ls -a        # 숨김 파일 포함 전체 보기
cd ..        # 상위 폴더 이동
```

### Git 기본 개념
- Working Directory
- Staging Area
- Repository

### Git 명령어
```bash
git init
git status
git add .
git add <파일명>
git commit
git log --oneline
git switch -c <브랜치명>
git push -u origin main
git push
```

</details>



<details>
<summary>2026-05-19 | uv · NumPy · Pandas 기초</summary>

### Python 환경 관리
- uv
- 가상환경(.venv)
- pyproject.toml
- uv.lock

### NumPy
- ndarray
- 벡터 연산
- 배열 인덱싱
- shape / dtype / ndim

### Pandas
- DataFrame 탐색
- head / info / describe
- loc / iloc
- 조건 필터링
- 결측치 처리
- groupby / agg 집계

### 실습
- Titanic 데이터 분석
- 생존율 분석
- 결측치 처리
- 그룹별 통계 분석

### Git 실습
```bash
git add .
git commit -m "feat: pandas 기초 실습 완료"
git push
```

</details>


<details>
<summary>2026-05-20 | EDA · matplotlib · plotly 데이터 시각화</summary>

### EDA (탐색적 데이터 분석)
- EDA 개념 및 데이터 탐색 흐름
- 데이터 분포 · 이상치 · 변수 관계 분석
- Anscombe’s Quartet 사례 분석
- 시각화 기반 데이터 해석

### 차트 선택 기준
- 히스토그램 (분포)
- 막대그래프 (비교)
- 산점도 (관계)
- 박스플롯 (이상치)
- 파이차트 (구성)
- 꺾은선그래프 (추세)

### matplotlib
- fig / ax 객체 구조
- plt.subplots()
- hist / bar / scatter / boxplot / pie
- tight_layout()
- savefig()
- 한글 폰트 설정

### plotly express
- px.histogram()
- px.scatter()
- px.line()
- px.bar()
- hover_name / hover_data
- marginal 옵션
- fig.write_html()

### 데이터 전처리
- pd.to_numeric(errors='coerce')
- 문자열 숫자 정제
- astype(str)
- str.split() / explode()
- 결측치 및 이상치 처리

### 실습
- Titanic 데이터 시각화
- IMDB Top 1000 분석
- 서울 아파트 실거래 데이터 분석
- 월별 거래 추이 시각화
- 구별 평균 거래가격 분석

### Git 실습
```bash
git add .
git commit -m "feat: 시각화 실습 완료"
git push
````

</details>


<details>
<summary>2026-05-21 | Streamlit · 인터랙티브 대시보드</summary>

### Streamlit 기초
- Streamlit 개념 및 실행 구조
- Python 기반 웹 앱 개발
- top-to-bottom rerun 모델
- 데이터 대시보드 프로토타이핑

### 환경 설정
- uv init
- uv add streamlit watchdog
- uv run streamlit run app.py
- watchdog 활용

### 기본 출력
- st.title()
- st.header()
- st.subheader()
- st.write()
- st.markdown()
- st.text()

### 위젯
- text_input
- selectbox
- slider
- checkbox
- multiselect
- button

### 사이드바
- st.sidebar
- 사용자 입력 필터 구성
- 데이터 조건 필터링
- 대시보드 레이아웃 분리

### 데이터 출력 및 시각화
- st.dataframe()
- st.metric()
- st.plotly_chart()
- Plotly 인터랙티브 차트 연동

### 레이아웃 구성
- st.columns()
- st.tabs()
- st.caption()
- st.divider()

### 캐시 최적화
- @st.cache_data
- rerun 성능 최적화
- .copy() 활용
- CachedObjectMutationWarning 대응

### 실습
- Titanic 필터 대시보드 제작
- IMDB 대시보드 제작
- 서울 아파트 대시보드 제작
- Plotly 기반 인터랙티브 차트 구성
- 사이드바 기반 데이터 필터링

### Git 실습
```bash
git add .
git commit -m "feat: Streamlit 대시보드 실습 완료"
git push
````

</details>


<details>
<summary>2026-05-26 | 머신러닝 개요 · 지도학습 파이프라인 · k-NN</summary>

### 머신러닝 개요

* AI · ML · DL 관계 이해
* 머신러닝과 전통 프로그래밍 차이
* 데이터 기반 학습 개념
* 패턴 학습 기반 예측 구조

### 머신러닝 학습 유형

* 지도학습 (Supervised Learning)
* 비지도학습 (Unsupervised Learning)
* 강화학습 (Reinforcement Learning)

### 지도학습

* 분류(Classification)
* 회귀(Regression)
* Feature / Label 개념
* Sample 개념
* 입력(X)과 정답(y) 구조 이해

### 비지도학습

* Clustering
* PCA(차원 축소)
* 이상 탐지(Anomaly Detection)

### 지도학습 파이프라인

* 데이터 수집
* 특성 선택
* train / test 분리
* 모델 학습
* 예측
* 평가

### train_test_split

* train / test 데이터 분리 이유
* 일반화(Generalization)
* 데이터 누수(Data Leakage)
* random_state
* stratify

### k-NN 알고리즘

* 거리 기반 분류 알고리즘
* KNeighborsClassifier
* k 값에 따른 성능 변화
* 다수결 기반 예측
* 최근접 이웃 개념

### scikit-learn 기본 패턴

```python
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()

kn.fit(X_train, y_train)

kn.predict(X_new)

kn.score(X_test, y_test)
```

### 데이터 시각화

* matplotlib scatter plot
* 도미 · 빙어 산점도 시각화
* 클래스 분포 시각화

### 실습

* 생선 데이터 분류
* 도미 / 빙어 분류 모델 구현
* train_test_split 적용
* k 값 비교 실습
* score 1.0 문제 분석
* 타이타닉 문제 정의 워크숍

### 주요 개념 정리

* Feature
* Label
* Training Set
* Test Set
* Generalization
* Classification
* Regression

### 오류 해결

* ModuleNotFoundError
* ValueError
* list index out of range
* random_state 재현성 문제
* matplotlib 그래프 출력 문제

### Git 실습

```bash
git add .
git commit -m "feat: 머신러닝 기초 및 k-NN 실습 완료"
git push
```

</details>



<details>
<summary>2026-05-27 | 회귀 알고리즘 · 특성 공학 · Ridge · Lasso</summary>

### StandardScaler

* 특성 스케일 차이 문제
* 유클리드 거리 왜곡
* 표준화(Standardization)
* z-score 공식
* 평균 0 / 표준편차 1 변환
* StandardScaler
* MinMaxScaler 비교

### Data Leakage

* 데이터 누설(Data Leakage)
* train 데이터 기준 스케일링
* fit / transform 차이
* 테스트 데이터 fit 금지
* 모델 평가 신뢰성 문제

### k-NN 회귀

* KNeighborsRegressor
* 분류와 회귀 차이
* 연속값 예측
* 이웃 평균 기반 예측
* 외삽(Extrapolation) 한계

### 회귀 평가 지표

* R² (결정계수)
* MAE (Mean Absolute Error)
* 평균 절대 오차
* 회귀 모델 성능 평가

### 선형 회귀

* LinearRegression
* coef_
* intercept_
* 직선 방정식
* 가중치(w)
* 편향(b)
* 외삽 가능성

### 손실 함수

* MSE (Mean Squared Error)
* 평균 제곱 오차
* 오차 제곱합 계산
* 손실 최소화 개념

### 경사 하강법

* Gradient Descent
* 비용 함수 최소화
* 학습률(alpha)
* 기울기 기반 최적화
* SGD 개념 연결

### 다항 회귀

* PolynomialFeatures
* degree 개념
* 곡선 회귀
* 특성 공학(Feature Engineering)
* 다중 회귀
* 교차항 생성

### 과적합 · 과소적합

* Overfitting
* Underfitting
* train/test R² 비교
* 학습 곡선 해석
* bias / variance 개념

### Ridge · Lasso

* 규제(Regularization)
* Ridge (L2 규제)
* Lasso (L1 규제)
* alpha 하이퍼파라미터
* 계수 축소
* 특성 선택 효과

### 하이퍼파라미터

* alpha
* n_neighbors
* degree
* Parameter vs Hyperparameter 차이

### 데이터 전처리

```python id="8p4kzs"
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

train_scaled = ss.fit_transform(train_input)

test_scaled = ss.transform(test_input)
```

### 회귀 모델 패턴

```python id="jv1mqo"
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

lr.predict(X_test)

lr.score(X_test, y_test)
```

### 다항 특성 생성

```python id="6weq9l"
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)

train_poly = poly.fit_transform(train_input)

test_poly = poly.transform(test_input)
```

### Ridge 실습

```python id="v8k3ma"
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=0.1)

ridge.fit(train_scaled, train_target)

ridge.score(test_scaled, test_target)
```

### Lasso 실습

```python id="4bq2nx"
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=10)

lasso.fit(train_scaled, train_target)

lasso.score(test_scaled, test_target)
```

### 실습

* 농어 무게 예측
* k-NN 회귀 실습
* 선형 회귀 실습
* PolynomialFeatures 실습
* degree 비교 실습
* Ridge alpha 탐색
* Lasso alpha 탐색
* 과적합 직접 실험
* train/test R² 비교 분석

### 주요 개념 정리

* Regression
* R²
* MSE
* Gradient Descent
* Learning Rate
* Overfitting
* Underfitting
* Regularization
* Ridge
* Lasso
* Hyperparameter
* Feature Engineering
* Data Leakage

### Git 실습

```bash id="1k4xpw"
git add .
git commit -m "feat: 회귀 알고리즘 및 규제 모델 실습 완료"
git push
```

</details>


<details>
<summary>2026-05-28 | 분류 알고리즘 · 평가지표 · bias/variance 진단</summary>

### LogisticRegression

* LogisticRegression
* 확률 기반 분류
* 선형 결합(z)
* Sigmoid 함수
* Softmax 함수
* 이진 분류(Binary Classification)
* 다중 분류(Multi Classification)

### Sigmoid 함수

* 시그모이드 함수
* 확률 변환
* decision_function
* predict_proba
* expit
* 결정 경계(Decision Boundary)

### Softmax

* 다중 클래스 확률 분포
* 클래스별 확률 계산
* Softmax 기반 분류
* 클래스 확률 합 = 1

### 분류 손실 함수

* Cross-Entropy
* Binary Cross-Entropy
* MSE와 분류 문제 차이
* 로그 손실(Log Loss)

### 분류 평가 지표

* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve
* AUC

### Confusion Matrix

* TP (True Positive)
* TN (True Negative)
* FP (False Positive)
* FN (False Negative)
* Type I Error
* Type II Error

### Precision · Recall · F1

* Precision / Recall Trade-off
* Threshold 개념
* 도메인별 평가 지표 선택
* 조화평균(F1)

### ROC-AUC

* ROC Curve
* TPR
* FPR
* AUC 해석
* 임계값 기반 평가

### bias / variance 진단

* High Bias
* High Variance
* Underfitting
* Overfitting
* train/test score 비교
* 일반화 성능 진단

### SGDClassifier

* 확률적 경사 하강법(SGD)
* partial_fit
* epoch 개념
* 조기 종료(Early Stopping)
* 배치 GD vs SGD 비교

### 데이터 전처리

* train_test_split
* StandardScaler
* stratify
* One-Hot Encoding
* pd.get_dummies()

### LogisticRegression 실습

```python id="xk8m1v"
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train, y_train)

lr.predict(X_test)

lr.predict_proba(X_test)
```

### Sigmoid 확인

```python id="9qp2zt"
from scipy.special import expit

decisions = lr.decision_function(X_test)

proba = expit(decisions)
```

### Confusion Matrix · 평가 지표

```python id="4hvm7r"
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score
)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

print(roc_auc_score(y_test, y_prob))
```

### SGDClassifier 실습

```python id="r8k1dc"
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(
    loss='log_loss',
    random_state=42
)

sc.partial_fit(
    train_scaled,
    train_target,
    classes=classes
)
```

### 실습

* 7종 생선 다중 분류
* LogisticRegression 실습
* Sigmoid 직접 확인
* Softmax 확률 출력
* Titanic 생존 분류
* Confusion Matrix 분석
* ROC-AUC 계산
* SGD epoch 그래프 분석
* Early Stopping 실습

### 주요 개념 정리

* Logistic Regression
* Sigmoid
* Softmax
* Cross-Entropy
* Decision Boundary
* Confusion Matrix
* Precision
* Recall
* F1 Score
* ROC-AUC
* Threshold
* SGD
* Epoch
* Early Stopping
* Bias / Variance

### 오개념 정리

* LogisticRegression은 회귀 모델이 아니라 분류 모델
* Accuracy만으로 모델 평가 불가
* Precision과 Recall은 Trade-off 관계
* fit() 반복은 epoch가 아님
* partial_fit() 기반 학습 필요

### Git 실습

```bash id="8bqv2j"
git add .
git commit -m "feat: 분류 알고리즘 및 평가지표 실습 완료"
git push
```

</details>


<details>
<summary>2026-05-29 | 결정 트리 · 앙상블 · 교차 검증 · 하이퍼파라미터 튜닝</summary>

### Decision Tree
- DecisionTreeClassifier
- Gini Impurity
- Entropy
- Information Gain
- Decision Boundary
- max_depth
- min_samples_split
- min_impurity_decrease
- Pruning (가지치기)

### Tree Analysis
- plot_tree()
- feature_importances_
- Root Node
- Decision Node
- Leaf Node

### Ensemble Learning
- Ensemble
- Bagging
- Bootstrap Sampling
- Random Forest
- OOB Score
- Feature Random Sampling

### Boosting
- Gradient Boosting
- HistGradientBoosting
- XGBoost
- LightGBM
- Learning Rate

### Cross Validation
- cross_validate()
- K-Fold Cross Validation
- StratifiedKFold
- Hold-out Validation
- CV Score

### Hyperparameter Tuning
- GridSearchCV
- RandomizedSearchCV
- Parameter Grid
- best_params_
- best_score_
- best_estimator_

### Bias / Variance Analysis
- High Bias (Underfitting)
- High Variance (Overfitting)
- Good Fit
- Train Score vs Test Score 비교

### 실습
- Wine Dataset 분류
- Decision Tree 모델링
- Random Forest 모델링
- K-Fold 교차 검증
- GridSearchCV 튜닝
- 최적 모델 평가

</details>

