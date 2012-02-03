# -*- coding: utf-8 -*-
import datetime
import unittest


class Authority(object):
    """
    The word "authority" is derived from the Latin word auctoritas, meaning invention, advice, opinion, influence, or command. In English, the word 'authority' can be used to mean power given by the state (in the form of Members of Parliament, Judges, Police Officers, etc.) or by academic knowledge of an area (someone can be an authority on a subject). The word "Authority" with capital "A", refers to the governning body upon which such authority (with lower case "a") is vested; for example, the Puerto Rico Electric Power Authority or the Massachusetts Bay Transportation Authority.
    """
    __source__ = 'http://en.wikipedia.org/wiki/Authority'
    __date__ = datetime.datetime(2012, 02, 02)

    def __init__(self, enforcement=None):
        self.enforcement = enforcement
        if self.enforcement is None:
            self.enforcement = False


class Citizen(object):
    """
    Citizenship is the state of being a citizen of a particular social, political, national, or human resource community. Citizenship status, under social contract theory, carries with it both rights and responsibilities. Citizenship was equated by Virginia Leary (1999) as connoting "a bundle of rights -- primarily, political participation in the life of the community, the right to vote, and the right to receive certain protection from the community, as well as obligations."[1] The group of all citizens is the citizenry.
    In law, citizenship denotes a link between an individual and a state. Under international law, citizenship is synonymous to nationality, although the two may have different meanings under national law. A person who does not have citizenship in any state is stateless.
    """
    __source__ = 'http://en.wikipedia.org/wiki/Citizen'
    __date__ = datetime.datetime(2012, 02, 02)

    def __init__(self, duties=None):
        self.duties = duties
        if self.duties is None:
            self.duties = []


class Institution(object):
    """
    An institution is any structure or mechanism of social order and cooperation governing the behavior of a set of individuals within a given human community. Institutions are identified with a social purpose and permanence, transcending individual human lives and intentions, and with the making and enforcing of rules governing cooperative human behavior.[1]
    The term "institution" is commonly applied to customs and behavior patterns important to a society, as well as to particular formal organizations of government and public service. As structures and mechanisms of social order among humans, institutions are one of the principal objects of study in the social sciences, such as political science, anthropology, economics, and sociology (the latter being described by Durkheim as the "science of institutions, their genesis and their functioning").[2] Institutions are also a central concern for law, the formal mechanism for political rule-making and enforcement.
    """
    __source__ = 'http://en.wikipedia.org/wiki/Institution'
    __date__ = datetime.datetime(2012, 02, 02)


class LegalCode(object):
    """
    A code is a type of legislation that purports to exhaustively cover a complete system of laws or a particular area of law as it existed at the time the code was enacted, by a process of codification.[citation needed] Though the process and motivations for codification are similar in common law and civil law systems, their usage is different. In a civil law country, a Code typically exhaustively covers the complete system of law.[citation needed] By contrast, in a common law country a Code is a less common form of legislation, which differs from usual legislation that, when enacted, modify the existing common law only to the extent of its express or implicit provision, but otherwise leaves the common law intact.[citation needed] By contrast, a code entirely replaces the common law in a particular area, leaving the common law inoperative unless and until the code is repealed.[dubious – discuss][citation needed]
    """
    __source__ = 'http://en.wikipedia.org/wiki/Legal_code'
    __date__ = datetime.datetime(2012, 02, 02)

    def __init__(self, form=None, rights=None):
        self.form = form
        if self.form is None:
            self.form = Authority()
        self.rights = rights # rights and freedoms to protect
        if self.rights is None:
            self.rights = []
        

class PoliticalPhilosophy(object):
    """
    Political philosophy is the study of such topics as politics, liberty, justice, property, rights, law, and the enforcement of a legal code by authority: what they are, why (or even if) they are needed, what, if anything, makes a government legitimate, what rights and freedoms it should protect and why, what form it should take and why, what the law is, and what duties citizens owe to a legitimate government, if any, and when it may be legitimately overthrown—if ever. In a vernacular sense, the term "political philosophy" often refers to a general view, or specific ethic, political belief or attitude, about politics that does not necessarily belong to the technical discipline of philosophy.[1]
    Political philosophy can also be understood by analysing it through the perspectives of metaphysics, epistemology and axiology. It provides insight into, among other things, the various aspects of the origin of the state, its institutions and laws.
    """
    __source__ = 'http://en.wikipedia.org/wiki/Political_philosophy'
    __date__ = datetime.datetime(2012, 02, 02)

    def __init__(self, origin=None, topics=None, laws=None, institutions=None, citizens=None, needed=None, legitimate=None, overthrowable=None):
        self.origin = origin
        assert self.origin is not None, 'Must specify an origin.'
        self.topics = topics
        if self.topics is None:
            self.topics = [
                'politics', 'liberty', 'justice', 
                'property', 'rights', 'law',
                ]
        self.laws = laws
        if self.laws is None:
            self.laws = [LegalCode()]
        self.institutions = institutions
        if self.institutions is None:
            self.institutions = [Institution()]
        self.citizens = citizens
        if self.citizens is None:
            self.citizens = [Citizen()]
        self.needed = needed
        if self.needed is None:
            self.needed = False # or True, why or why not?
        self.legitimate = legitimate
        if self.legitimate is None:
            self.legitimate = True # or False, why or why not?
        self.overthrowable = overthrowable
        if self.overthrowable is None:
            self.overthrowable = True # legitimate to overthrow

        
class TestPoliticalPhilosophy(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def runTest(self):
        origins = [
            # about politics that does not necessarily
            # belong to the technical discipline of philosophy.
            'general view',
            'ethic',
            'belief',
            'attitude',
            # can also be understood 
            # by analysing it 
            # through the perspectives of 
            'metaphysics',
            'epistemology',
            'axiology',
        ]
        self.assertRaises(AssertionError, PoliticalPhilosophy) # Must specify an origin.
        for origin in origins:
            politicalPhilosophy = PoliticalPhilosophy(origin=origin)
            self.assertIsInstance(politicalPhilosophy.topics, list)
            self.assertIsInstance(politicalPhilosophy.laws, list)
            self.assertIsInstance(politicalPhilosophy.institutions, list)
            self.assertIsInstance(politicalPhilosophy.citizens, list)
            self.assertTrue(politicalPhilosophy.legitimate)
            self.assertFalse(politicalPhilosophy.needed)
            self.assertTrue(politicalPhilosophy.overthrowable)


if __name__ == '__main__':
    unittest.main()