__author__ = 'yutao'


class Contact(object) :
    def __init__(self):
        self.position = ""
        self.phone = ""
        self.email = ""
        self.fax = ""
        self.affiliation = ""
        self.address = ""
        self.intr = ""
        self.edu =""
        self.work = ""
        self.bio = ""
        self.homepage = ""
        pass

    def from_mongo(self,data):
        if data is not None:
            self.position = data.get("position",None)
            self.phone = data.get("phone",None)
            self.email = data.get("email",None)
            self.fax = data.get("fax",None)
            self.affiliation = data.get("affiliation",None)
            self.address = data.get("address",None)
            self.intr = data.get("intr",None)
            self.edu = data.get("edu",None)
            self.work = data.get("work",None)
            self.bio = data.get("bio",None)
            self.homepage = data.get("homepage",None)

    def to_dict(self):
        dump = {}
        dump["position"] = self.position
        dump["phone"] = self.phone
        dump["email"] = self.email
        dump["fax"] = self.fax
        dump["affiliation"] = self.affiliation
        dump["address"] = self.address
        dump["intr"] = self.intr
        dump["edu"] = self.edu
        dump["work"] = self.work
        dump["bio"] = self.bio
        dump["homepage"] = self.homepage
        return dump

class Person(object):
    def __init__(self):
        self.id = -1
        self.names = ""
        self.name = ""

        self.type = ""
        self.contact_id = -1
        self.email = ""
        self.address = ""
        self.phone = ""
        self.fax = ""
        self.homepage = ""
        self.position = ""
        self.affiliation = ""

        self.phduniv = ""
        self.phdmajor = ""
        self.phddate = ""
        self.msuniv = ""
        self.msmajor = ""
        self.msdate = ""
        self.bsuniv = ""
        self.bsmajor = ""
        self.bsdate = ""
        self.bio = ""
        self.interest = ""
        self.code = []
        self.nsfc = None
        self.reviewer = 0

        self.img = ""

        self.h_index = 0
        self.g_index = 0
        self.org = ""
        self.pub_ids = 0
        self.tags = []
        self.n_citation = 0
        self.n_pubs = 0
        self.sociability = 0
        self.activity = 0
        self.rising_star = 0
        self.new_star = 0

        self.pubs = []
        self.years = []

        self.url = ""

        self.contact = Contact()


    def from_mongo(self, item):
        data = item
        self.id = str(item['_id'])
        self.names = data['names']
        self.name = data["name"]
        self.h_index = data['h_index']
        self.g_index = data['g_index']
        self.orgs = data["orgs"]
        self.org = data.get("org", "")
        self.pub_ids = [p["i"] for p in data["pubs"]]
        self.tags = data.get("tags", [])[:5]
        self.n_citation = data["n_citation"]
        self.n_pubs = data["n_pubs"]
        self.h_index = data["h_index"]
        self.g_index = data["g_index"]
        self.sociability = data["sociability"]
        self.activity = data["activity"]
        self.rising_star = data.get("rising_star", 0)
        self.new_star = data["new_star"]
        self.hide = data.get("hide", False)
        self.score = item.get("_score", 0)

        self.contact = Contact().from_mongo(item.get("contact",None))
        return self


    def to_dict(self):
        dump = {}

        dump["id"] = self.id
        dump["names"] = self.names
        dump["name"] = self.name

        dump["h_index"] = self.h_index
        dump["g_index"] = self.g_index
        dump["org"] = self.org
        dump["pub_ids"] = self.pub_ids
        dump["tags"] = self.tags
        dump["n_citation"] = self.n_citation
        dump["n_pubs"] = self.n_pubs
        dump["sociability"] = self.sociability

        dump["activity"] = self.activity
        dump["rising_star"] = self.rising_star
        dump["new_star"] = self.new_star

        dump["score"] = self.score

        dump["img"] = self.img

        dump["pubs"] = [p.to_dict() for p in self.pubs]
        dump["years"] = self.years

        dump["contact"] = self.contact.to_dict()

        return dump