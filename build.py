print('static site') 

# Reads in the top.html 
 
print('reading in html variables')

top_html = open('./templates/topindex.html').read()

#Reads in the bottom.html

bottom_html = open('./templates/bottomindex.html').read() 

# Reads in the middle 

middle_html = open('./content/index.html').read() 

print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)




# Assembles the new index.html file 
# by combining the top middle and bttom in that order
# Writes the new index.html file to a brand new file
# in the same directory

open('index.html','w+').write(combined_html)


print('static site') 

# Reads in the top.html 

print('reading in html variables')

top_html = open('./templates/topAboutMe.html').read()

#Reads in the bottom.html

bottom_html = open('./templates/bottomAboutMe.html').read() 

# Reads in the middle 

middle_html = open('./content/AboutMe.html').read() 

print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)




# Assembles the new index.html file 
# by combining the top middle and bttom in that order
# Writes the new index.html file to a brand new file
# in the same directory

open('AboutMe.html','w+').write(combined_html)



print('static site') 

# Reads in the top.html 

print('reading in html variables')
top_html = open('./templates/topBlog.html').read()

#Reads in the bottom.html

bottom_html = open('./templates/bottomBlog.html').read() 

# Reads in the middle 

middle_html = open('./content/Blog.html').read() 

print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)




# Assembles the new index.html file 
# by combining the top middle and bttom in that order
# Writes the new index.html file to a brand new file
# in the same directory

open('Blog.html','w+').write(combined_html)

print('static site') 

# Reads in the top.html 

print('reading in html variables')
top_html = open('./templates/topProjects.html').read()

#Reads in the bottom.html

bottom_html = open('./templates/bottomProjects.html').read() 

# Reads in the middle 

middle_html = open('./content/Projects.html').read() 

print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)




# Assembles the new index.html file 
# by combining the top middle and bttom in that order
# Writes the new index.html file to a brand new file
# in the same directory

open('Projects.html','w+').write(combined_html)

