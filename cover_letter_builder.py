company = 'Company name'
position = 'Staff Software Engineer'
COVER_LETTER = 'Dear Sir or Madam, \n\n' \
               'I would like to apply for an open position within {company} as a {position}. ' \
               'I have the skills and experience to bring excellence to this position.\n\n' \
               'Over the past 12 years, I have been working in the IT industry, and more than 6 years as a programmer and ' \
               'have the competence of a system administrator (TCP/IP, Linux, Windows). ' \
               'I have always been attracted to complex analytical tasks. In the course of my work, ' \
               'I regularly engaged in the design of automated systems using mathematical methods, for example, ' \
               'I made a model of the warehouse management system, which distributes all warehouse flows without ' \
               'human involvement. I am very eager to join {company} and use my key skills ' \
               'and experience for the development of the organization.\n\n' \
               'I am currently living in Austin TX. I have a U.S. work permit, Texas ID and SSN.\n\n' \
               'My resume is enclosed for your review. I am available for an interview at your convenience ' \
               'and can be reached at <PHONE NUMBER>. I look forward to discussing with you the contributions ' \
               'I know I can make to {company} as a {position}.\n\n' \
               'Thank you for your time and consideration.\n\n' \
               'Yours sincerely,\n<FIRSTNAME LASTNAME>.'.format(company=company, position=position)

print(COVER_LETTER)