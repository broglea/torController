torController
=============

A very simple and basic python torController that uses telnet to the localhost to authenticate and get new identities

        PREREQUISITE TO USING THIS:
            1) You must edit your /etc/tor/torrc file to turn on ControlPort (default is 9051) 
            2) You must edit your /etc/tor/torrc with your HashedControlPassword you want to use,
               this can be obtained via the command 'tor --hash-password passwordGoesHere'

        Usage:
            from torController import torController
            tor = torController(9051, "passwordGoesHere")
            tor.connect()
            tor.newIdentity()        <- Gets a new identity using any random country
            tor.newIdentity("US")    <- Gets a new identity from specified 2 letter ISO country code
