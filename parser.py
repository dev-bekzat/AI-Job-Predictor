import csv
from bs4 import BeautifulSoup

html_mock = '''
<html>
  <body>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Python Backend Developer</h2>
      <ul class="skills">
        <li>Python</li><li>Django</li><li>REST APIs</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Machine Learning Engineer</h2>
      <ul class="skills">
        <li>TensorFlow</li><li>Scikit-learn</li><li>Python</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Data Analyst</h2>
      <ul class="skills">
        <li>SQL</li><li>Excel</li><li>Power BI</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">DevOps Engineer</h2>
      <ul class="skills">
        <li>Linux</li><li>Docker</li><li>CI/CD</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Frontend Developer</h2>
      <ul class="skills">
        <li>JavaScript</li><li>React</li><li>HTML/CSS</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Java Developer</h2>
      <ul class="skills">
        <li>Java</li><li>Spring Boot</li><li>MySQL</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Project Manager</h2>
      <ul class="skills">
        <li>Agile</li><li>Scrum</li><li>Jira</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">UX/UI Designer</h2>
      <ul class="skills">
        <li>Figma</li><li>UX Research</li><li>Wireframing</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">QA Engineer</h2>
      <ul class="skills">
        <li>Test Cases</li><li>Postman</li><li>Selenium</li>
      </ul>
    </div>
    <div class="job_seen_beacon">
      <h2 class="jobTitle">Content Specialist</h2>
      <ul class="skills">
        <li>Copywriting</li><li>SEO</li><li>Analytics</li>
      </ul>
    </div>
  </body>
</html>
'''

soup = BeautifulSoup(html_mock, 'html.parser')
jobs = soup.find_all("div", class_="job_seen_beacon")

# into csv
with open("my_custom_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["skills", "Job Title"])
    for job in jobs:
        title = job.find("h2", class_="jobTitle").text.strip()
        skills = [li.text.strip() for li in job.find("ul", class_="skills").find_all("li")]
        writer.writerow([", ".join(skills), title])

print("Job data written to my_custom_data.csv")