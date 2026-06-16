# [직업명, 관련과목, 협업, 창의성, 문제해결, 데이터분석]
jobs = [
    # 수학 관련
    ["AI 데이터 전문가", "수학", "Y", "N", "Y", "Y"],
    ["소프트웨어 개발자", "수학", "Y", "Y", "Y", "N"],
    
    # 과학 관련
    ["생명과학 연구원", "과학", "N", "N", "Y", "Y"],
    ["로봇 공학자", "과학", "Y", "Y", "Y", "N"],
    
    # 사회 관련
    ["마케팅 기획자", "사회", "Y", "Y", "N", "Y"],
    ["심리 상담 전문가", "사회", "N", "N", "N", "Y"],
    
    # 국어 관련
    ["초등 교사", "국어", "Y", "N", "N", "N"],
    ["콘텐츠 작가", "국어", "N", "Y", "Y", "N"],
    
    # 예술(미술/음악) 관련
    ["UX/UI 디자이너", "예술", "Y", "Y", "N", "Y"],
    ["영상 크리에이터", "예술", "N", "Y", "Y", "N"]
]

def get_user_input():
    print("\n--- 미래 직업 적성 검사를 시작합니다 ---")
    
    # [보완] 지정된 5개 과목 외의 단어를 입력하면 무한 루프로 차단합니다.
    while True:
        subject = input("좋아하는 과목을 입력하세요 (국어/수학/사회/과학/예술): ").strip()
        if subject in ["국어", "수학", "사회", "과학", "예술"]:
            break
        print("잘못된 입력입니다. 안내된 5개 과목 중에서 선택해 주세요.")

    # [질문 1] 협업 선호
    while True:
        team = input("팀으로 협업하는 활동을 좋아하시나요? (Y/N): ").upper().strip()
        if team in ["Y", "N"]: break
        print("잘못된 입력입니다. Y 또는 N으로 입력해 주세요.")

    # [질문 2] 창의성 선호
    while True:
        creative = input("새로운 아이디어를 내는 활동을 좋아하시나요? (Y/N): ").upper().strip()
        if creative in ["Y", "N"]: break
        print("잘못된 입력입니다. Y 또는 N으로 입력해 주세요.")

    # [질문 3] 문제 해결 선호
    while True:
        problem = input("논리적인 문제를 푸는 걸 좋아하시나요? (Y/N): ").upper().strip()
        if problem in ["Y", "N"]: break
        print("잘못된 입력입니다. Y 또는 N으로 입력해 주세요.")

    # [질문 4] 데이터/분석 선호
    while True:
        data = input("수치나 정보를 정리하고 분석하는 걸 좋아하시나요? (Y/N): ").upper().strip()
        if data in ["Y", "N"]: break
        print("잘못된 입력입니다. Y 또는 N으로 입력해 주세요.")    

    return [subject, team, creative, problem, data]

def find_best_job(job_list, user_info):
    best_jobs = []  # [보완] 동점자를 모두 담기 위해 리스트로 변경
    max_score = -1
    
    user_subject  = user_info[0]
    user_team     = user_info[1]
    user_creative = user_info[2]
    user_problem  = user_info[3]
    user_data     = user_info[4]
    
    for job in job_list:
        score = 0  
        
        if job[1] == user_subject: score += 2  
        if job[2] == user_team: score += 1     
        if job[3] == user_creative: score += 1  
        if job[4] == user_problem: score += 1   
        if job[5] == user_data: score += 1      
        
        # [보완] 더 높은 점수가 나오면 리스트를 비우고 새로 시작
        if score > max_score:
            max_score = score
            best_jobs = [job[0]] 
        # [보완] 기존 최고 점수와 동점이면 추천 후보 리스트에 추가
        elif score == max_score:
            best_jobs.append(job[0])
            
    # 동점 직업들 중 여러 개가 나오면 콤마(',')로 연결해서 문자열로 반환
    return ", ".join(best_jobs), max_score

def print_result(best_job, max_score):
    print("\n" + " 분석 진행 중... 📊 ".center(38, "-"))
    print("\n" + "=[ 적성 검사 결과 ]=".center(36, " "))
    print(f" ▶ 당신에게 가장 추천하는 미래 직업: [ {best_job} ]")
    print(f" ▶ 매칭 적합도 점수: {max_score} / 6 점")
    print("="*40)

def main():
    while True:
        user_info = get_user_input()
        best_job, max_score = find_best_job(jobs, user_info)
        print_result(best_job, max_score)
        
        # [보완] 재실행 시에도 한영키 오타(ㅛ) 및 미세 공백 허용
        retry = input("\n검사를 다시 하시겠습니까? (Y/N): ").upper().strip()
        if retry not in ["Y", "ㅛ"]:
            print("\n프로그램을 종료합니다. 당신의 진로를 응원합니다! 🚀")
            break
            
if __name__ == "__main__":
    main()