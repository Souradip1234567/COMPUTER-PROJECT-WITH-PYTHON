while(True): 
     print("Press 1 to  get student     details") 
     print("Press 2 to  get course      details") 
     print("Press 3 to  get batch       details") 
     print("Press 4 to  get department  details") 
     print("Press 5 to  get examination details") 
     print("Press 0 to stop") 
     choice = int(input("Enter your choice: ")) 
     if(choice == 0): 
         break 
     elif(choice== 1): 
         from student import * 
         while(True): 
             print("Press 1 to create a student") 
             print("Press 2 to update a student's details") 
             print("Press 3 to remove a student") 
             print("Press 4 to generate report card of a student") 
             print("Press 0 to return back to main menu") 
             ch = int(input("Enter your choice: ")) 
             if(ch == 0): 
                 break 
             elif(ch == 1): 
                 student_id = input("Enter student ID: ") 
                 student_name = input("Enter student name: ") 
                 createStudent(student_id, student_name) 
             elif(ch== 2): 
                 ostudent_id = input("Enter old student ID: ") 
                 updateStudent(ostudent_id) 
             elif(ch== 3): 
                 student_id = input("Enter student ID: ") 
                 removeStudent(student_id) 
             elif(ch== 4): 
                 student_id = input("Enter student ID: ") 
                 reportCard(student_id) 
             else: 
                 print("Invalid input. Try again.")   
     elif(choice == 2): 
         from course import * 
         while(True): 
             print("Press 1 to create a course") 
             print("Press 2 to view performance of students on the course") 
             print("Press 3 to show all course statistics as histogram") 
             print("Press 0 to return back to main menu") 
             y1 = int(input("Enter your choice: ")) 
             if(y1 == 0): 
                 break 
             elif(y1 == 1): 
                 course_id = input("Enter your course ID: ") 
                 course_name = input("Enter  the course name: ") 
                 createCourse(course_id, course_name) 
             elif(y1 == 2): 
                 course_id = input("Enter course ID: ") 
                 checkPerformance(course_id) 
             elif(y1 == 3): 
                 student_id = input("Enter course ID: ") 
                 courseStatistics(course_id) 
             else: 
                 print("Invalid input. Try again.") 
     elif(choice == 3): 
         from batch import * 
         while(True): 
             print("Press 1 to create a batch") 
             print("Press 2 to view all the students in a batch") 
             print("Press 3 to show all the courses in a batch") 
             print("Press 4 to view performance of all the students in a batch") 
             print("Press 5 to view pie chart of percentage all the students in a batch") 
             print("Press 0 to return to main menu") 
             z = int(input("Enter your choice: ")) 
             if(z == 0): 
                 break 
             elif(z == 1): 
                 batch_name = input("Enter batch name: ") 
                 createBatch(batch_name) 
             elif(z == 2): 
                 batch_id = input("Enter batch ID: ") 
                 viewStudents(batch_id) 
             elif(z == 3): 
                 batch_id = input("Enter batch ID: ") 
                 viewCourses(batch_id) 
             elif(z == 4): 
                 batch_id = input("Enter batch ID: ") 
                 viewPerformance(batch_id) 
             elif(z == 5): 
                 batch_id = input("Enter batch ID: ") 
                 pieChart(batch_id) 
             else: 
                 print("Invalid input. Try again.") 
     elif(choice == 4): 
         from department import * 
         while(True): 
             print("Press 1 to create a department") 
             print("Press 2 to view all betches in a department") 
             print("Press 3 to view average performance of all betches in a department") 
             print("Press 4 to view line plot of department statistics") 
             print("Press 0 to return to main menu") 
             y = int(input("Enter your choice: ")) 
             if(y == 0): 
                 break 
             elif(y == 1): 
                 department_id = input("Enter department ID: ") 
                 department_name = input("Enter department name: ") 
                 createDepartment(department_id, department_name) 
             elif(y == 2): 
                 department_id = input("Enter department ID: ") 
                 viewBatches(department_id) 
             elif(y == 3): 
                 department_id = input("Enter department ID: ") 
                 viewPerformanceD(department_id) 
             elif(y == 4): 
                 department_id = input("Enter department ID: ") 
                 linePlot(department_id) 
             else: 
                 print("Invalid input. Try again.") 
     elif(choice == 5): 
         from examination import * 
         while(True): 
             print("Press 1 to enter marks of all students for an exam") 
             print("Press 2 to view performance of all students in an exam") 
             print("Press 3 to show examination statistics as a scatter plot") 
             print("Press 0 to return back main menu") 
             c = int(input("Enter your choice: ")) 
             if(c == 0): 
                 break 
             elif(c == 1): 
                 course_id = input("Enter course ID: ") 
                 enterMarks(course_id) 
             elif(c == 2): 
                 course_id = input("Enter course ID: ") 
                 viewPerformanceE(course_id) 
             elif(c == 3): 
                 scatterPlot() 
             else: 
                 print("Invalid input. Try again.") 
      
        
