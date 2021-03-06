# 2.1 phase 1
# def main():
#     topAboutMe = open("templates/topAboutMe.html").read()
#     topBlog = open("templates/topBlog.html").read()
#     topProjects = open("templates/topProjects.html").read()
#     topindex = open("templates/topindex.html").read()
#     about_me = open("content/AboutMe.html").read()
#     blog = open("content/Blog.html").read()
#     projects = open("content/Projects.html").read()
#     index = open("content/index.html").read()
#     templatesAboutMe = open("templates/bottomAboutMe.html").read()
#     templatesBlog = open("templates/bottomBlog.html").read()
#     templatesProjects = open("templates/bottomProjects.html").read()
#     templatesindex = open("templates/bottomindex.html").read()    
# #to invoke
# if main =="__main__":
#     main()
    
# 2.2 phase 2 

pages = [
    {
        "filename": "AboutMe.html",
        "title": "About Me",
     },
    {
        "filename": "Blog.html",
        "title": "Blog",
     },
     {
        "filename": "Projects.html",
        "title": "Projects",
     },
     {
        "filename": "index.html",
        "title": "index",
     },
     
]

# 2.3 phase 3

# start = open("templates/topAboutMe.html").read()
# end = open("templates/bottomAboutMe.html").read()
# full = start + end
# open("baseAboutMe.html", "w+").write(full)

# start = open("templates/topProjects.html").read()
# end = open("templates/bottomProjects.html").read()
# full = start + end
# open("baseProjects.html", "w+").write(full)

# start = open("templates/topBlog.html").read()
# end = open("templates/html.bottomBlog").read()
# full = start + end
# open("baseBlog.html", "w+").write(full)

# start = open("templates/topindex.html").read()
# end = open("templates/bottomindex.html").read()
# full = start + end
# open("baseindex.html", "w+").write(full)


# 2.4 phase 4

# def apply_template(content):

#     return results

# def main():
#     content = open("docs/baseindex.html")
#     content = open("docs/baseAboutMe.html")
#     content = open("docs/baseProjects.html")
#     content = open("docs/baseBlog.html")
#     resulting_html_for_base = apply_template(content)
    
# 2.5 phase 5

def apply_template(content, title):
    top = open("templates/top.html").read()
    bottom = open("templates/bottom.html").read()
    # template = open("docs/baseBlog.html").read()
    # template = open("docs/baseAboutMe.html").read()
    # index_html = template.replace("{{content}}", value)
    title_replace = top.replace("{{ title }}", title)
    rendered_page = top + content + bottom
    return (rendered_page)
   
def main():
    for value in pages:
        content = open("content/" + value["filename"]).read()
        title = value["title"]
        resulting_html_for_index = apply_template(content, title)
        open("docs/" + value["filename"], "w+").write(resulting_html_for_index)
    
if __name__ == "__main__":
    main()
    
# HW 4 starts here 

# 2.1.1 phase 1

# import glob
# all_html_files = glob.glob('content/*.html')
# print(all_html_files)

# # 2.1.2 phase 1

# import os

# file_path = "content/blog1.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)

# # 2.1.3 phase 1

# pages = []
# def html_output():
#     for each in all_html_files:
#         file_name = os.path.basename(each)
#         name_only, extension = os.path.splitext(file_name)
        
      
#         pages.append({
#             "filename": file_name,
#             "title": name_only,
#             "output": "docs/" + name_only + '.html',
#             "link": name_only + '.html',
#              })
        
# def apply_template():
#     for page in pages:
#         index_html = open(page['filename']).read()
#         template_html = open('templates/base.html').read()
#         template = Template(template_html)
#         page_output = template.render(
#             title=page['title'],
#             content=index_html,
#             pages=pages,
#             )
#     data = open(page["output"], "w+")
#     data.write(page_output)
#     data.close()  

# # 2.2.2 phase 2

# from jinja2 import Template
# index_html = open("docs/index.html").read()
# template_html = open("base.html").read()
# template = Template(template_html)
# template.render(
# title="Homepage",
# content=index_html
# )

# # 2.3.1 phase 3



# template.render(pages=pages, content='AboutMe.html')
# template.render(pages=pages, content='Projects.html')
# template.render(pages=pages, content='Blog.html')
