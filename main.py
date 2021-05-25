import requests

loginDomain = 'https://euidp.aholddelhaize.com/isam/sps/auth?PartnerId=az_ahsam'
betweenDomain = 'https://sam.ah.nl'
scheduleDomain = 'https://sam.ahold.com/wrkbrn_jct/etm/etmMenu.jsp'
credentials = {
    'username': 'pnlxxxxx',
    'password': 'qwerty12345'
}
# workflow:
# 1.log in to sam.ah.nl
# 2.go to scheduleDomain
# 3.press 'Start'
# 3.get every cell with class name 'calendarCellRegularFuture'
# 4.Get the time and location from every cell
# 5.Check up to one month in the future

with requests.Session() as session:
    p = session.post(loginDomain, data=credentials)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(p.text)
    print(" \n \n \n \n \n \n")

    # An authorised request.
    req = session.get(betweenDomain)
    req2 = session.get(scheduleDomain)
    print(req.text)
    print(" \n \n \n \n \n \n")
    print(req2.text)
