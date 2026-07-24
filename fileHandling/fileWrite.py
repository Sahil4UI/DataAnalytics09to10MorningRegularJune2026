data = '''
3. Manual Copy (Bilkul Free)
LocalWP me:
app/public (ya app/public_html) ke andar ki saari WordPress files zip kar lo.
phpMyAdmin se database export kar lo.
Hosting me:
Saari files public_html me upload karo.
Database create karo.
SQL import karo.
wp-config.php me database name, username, password update karo.
URLs replace karo (Better Search Replace plugin ya WP-CLI se).
'''

# method1
'''
file = open("abc.txt","w")
file.write(data)
file.close()
'''

#method2
with open("abc.txt","w") as file:
    file.write(data)
