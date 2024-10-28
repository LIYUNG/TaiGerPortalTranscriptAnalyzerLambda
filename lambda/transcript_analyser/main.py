import sys
import json
from database.ElectricalEngineering.EE_sorter import EE_sorter
from database.general_sorter import general_sorter_function

def analyze_transcript(str_courses, category, student_id, student_name, language, str_courses_taiger_guided, requirement_ids="[]"):
    print("--------------------------")
    print("New Transcript Analyser")
    print("Python version:")
    print(sys.version)
    print("--------------------------")

    # print course:
    course = json.loads(str_courses)
    course_arr = json.loads(course)
    courses_taiger_guided = json.loads(str_courses_taiger_guided)
    courses_taiger_guided_arr = json.loads(courses_taiger_guided)
    requirement_ids_arr = json.loads(requirement_ids)
    course_arr = course_arr + courses_taiger_guided_arr
    print("requirement_ids_arr", requirement_ids_arr)

    general_sorter_function(
        course_arr, student_id, student_name, language, requirement_ids_arr)
    
    # 
    # sorter_functions = {
    #     'ee': EE_sorter,
    # }
    # program_code = category
    # if program_code in sorter_functions:
    #     sorter_functions[program_code](
    #         course_arr, student_id, student_name, language)

    return {str_courses, category, student_id, student_name, language, str_courses_taiger_guided}


if __name__ == "__main__":
    analyze_transcript(sys.argv[1], sys.argv[2], sys.argv[3],
                       sys.argv[4], sys.argv[5], sys.argv[6])
