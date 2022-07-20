
html_head = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ausdruck</title>
    <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;}
        .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
          overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
          font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-186s{border-color:inherit;font-size:medium;text-align:left;vertical-align:top}
        .tg .tg-y698{background-color:#efefef;border-color:inherit;text-align:left;vertical-align:top}
        .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}



        @media print {
          .hidden-print {
            box-shadow: none !important;
            border: none !important;
            break-inside: avoid !important;
          }

          .description-title{
            visibility:hidden;
          }
        }
        
      html, body { height: 99%; }


        </style>
</head>
<body>'''

html_page_template = '''<body>
    <div class="page-marker hidden-print" style="word-wrap: break-word; margin-bottom: 20px; margin-left: auto; margin-right: auto; width: 700px; padding-bottom: 15px; border :1px solid black;  box-shadow: 10px 10px 8px #888888;">
    <div style="margin: auto; page-break-after: always;width: 683px;">
        <h1 style="text-align: center;padding-bottom: 15px;">Registrierung von Personen gem. §7 Abs. 5 TestV</h1>
        
        <h3 style="text-align: left;">{{Ressource}}</h3>
        <div">
            <table class="tg" style="table-layout: fixed; width: 679px; margin: auto;">
            <colgroup>
            <col style="width: 266px">
            <col style="width: 413px">
            </colgroup>
            <thead>
              <tr>
                <th class="tg-186s">Datum/Uhrzeit:</th>
                <th class="tg-186s">{{Termine}}</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="tg-186s">Testgrund (TestV):</td>
                <td class="tg-186s">{{Grund}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Testart:</td>
                <td class="tg-186s">{{Testart}}<br><br>{{ID}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Name:</td>
                <td class="tg-186s">{{GF_Familienname}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Vorname:</td>
                <td class="tg-186s">{{GF_Vorname}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Geburtsdatum:</td>
                <td class="tg-186s">{{GF_Geburtsdatum}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Straße:</td>
                <td class="tg-186s">{{GF_Strasse}} {{GF_Hausnr}}</td>
              </tr>
              <tr>
                <td class="tg-186s">PLZ / Ort:</td>
                <td class="tg-186s">{{GF_PLZ}} {{GF_Ort}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Telefon:</td>
                <td class="tg-186s">{{GF_Telefon}}</td>
              </tr>
              <tr>
                <td class="tg-186s">E-Mail:</td>
                <td class="tg-186s">{{GF_Email}}</td>
              </tr>
              <tr>
                <td class="tg-186s">Sonstiges:</td>
                <td class="tg-186s"><p style="font-weight:bold;font-size: 25px;font-style:italic; text-align: center !important;margin: 0px !important">{{Testnummer}}</p></td>
              </tr>
              <tr>
                <td class="tg-y698"></td>
                <td class="tg-y698"></td>
              </tr>
              <tr>
                <td class="tg-186s"> Befund bzw.<br>PCR-Code</td>
                <td class="tg-0pky">
                    <table style="width: 80%; margin: auto;">
                        <tr>
                        <td style="width: 20px;">
                            
                        </td>
                        
                        <td style="border: none;" >
                            negativ
                        </td> 

                        <td style="width: 20px; ">
                               
                        </td>

                        <td style="border: none;">
                            positiv
                        </td>
                        </tr>
                    </table>
                    </td>
              </tr>
              <tr>
                <td class="tg-y698"></td>
                <td class="tg-y698"></td>
              </tr>
              <tr>
                <td class="tg-186s">Die Durchführung des Tests wird hiermit bestätigt! <br></td>
                <td class="tg-0pky">
                    <p style="margin-top: 35px; margin-bottom: 0px;text-align: center;">
                        ____________________________ <br>
                        <span style="font-size: smaller;">Unterschrift der getesteten Person</span> 
                    </p>
                </td>
              </tr>
              <tr>
                <td class="tg-186s">Unterschrift der die Testung<br>durchführenden Person:</td>
                <td class="tg-0pky"><br><br><br></td>
              </tr>
            </tbody>
            </table>
        </div>
    </div>
 
     </div>
  '''

html_selbstauskunft = """


      <div class="page-marker hidden-print" style="word-wrap: break-word; margin-bottom: 20px; margin-left: auto; margin-right: auto; width: 700px; padding-bottom: 15px; border :1px solid black;  box-shadow: 10px 10px 8px #888888;">

      <div style="margin:1em; font-size: small; page-break-after: always;width: 683px;">
    <div>
      <table >
        <tr>
          <td>
        <h3 style="display: inline;">Selbstauskunft/Nachweis nach § 6 Abs. 3 Nr. 4 und 5 TestV zur Inanspruchnahme von Testungen nach § 4a TestV</h3>
       </td>
       <td>
        <h1>{{Testnummer}}</h1>
       </td>
        </tr>
      </table>
        <div>
           <p style="margin-top: 0px;">
            Nachweis der Identität: 
           

            <input style="margin-left: 0.5em;" type="checkbox" name="" id=""><label style="margin-left: 0.5em;"  for="">Personalausweis</label>
            
            <input style="margin-left: 0.5em;"  type="checkbox" name="" id=""><label style="margin-left: 0.5em;"  for="">Reisepass Ausweisnummer: </label>
            
            <input style="margin-left: 0.5em;" size="25em;" value="______________" type="text" name="" id="">
          </p> 
        </div>

        <p>Hiermit versichere ich,
        <input size="35em;" type="text" value="{{GF_Vorname}} {{GF_Familienname}}">
      </p>
        <span>geboren am</span>
        <input type="text" size="12em;" value="{{GF_Geburtsdatum}}">
        <span>in</span>
        <input type="text" name="" id="">
         wohnhaft in 
        <input type="text" value="{{GF_PLZ}} {{GF_Ort}}">
    </div>

    <div>
        dass ich zu folgender Personengruppe gehöre:
        <div>


            <style type="text/css">
                .tg  {border-collapse:collapse;border-spacing:0;}
                .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;;
                  overflow:hidden;padding:10px 5px;word-break:normal;}
                .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;;
                  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
                .tg .tg-1lax{text-align:left;vertical-align:top; font-size: smaller; min-width: 2em;}
                </style>
                 <table class="tg">
                <thead>
                  <tr>
                    <th class="tg-1lax">{{X1}}</th>
                    <th class="tg-1lax">Personen, die zum Zeitpunkt der Testung das fünfte Lebensjahr noch nicht vollendet haben (§ 4a Absatz 1 Nr. 1 TestV)* <br>
                        <label for="">Name & Geburtsdatum des Kindes </label> <input type="text" size="40em;">
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="tg-1lax">{{X2}}</td>
                    <td class="tg-1lax">Personen, die nicht gegen das Coronavirus geimpft werden können oder in den letzten drei Monaten nicht geimpft werden konnten<br> (aus medizinischen Gründen oder wegen Schwangerschaft im ersten Schwangerschaftsdrittel) nach § 4a Absatz 1 Nr. 2 TestV*</td>
                  </tr>
                  <tr>
                    <td class="tg-1lax">{{X3}}</td>
                    <td class="tg-1lax">Teilnehmer von Impfwirksamkeitsstudien nach § 4a Abs. 1 Nr. 3 TestV*</td>
                  </tr>
                  <tr>
                    <td class="tg-1lax">{{X4}}</td>
                    <td class="tg-1lax">Isolierte Personen zur Beendigung der Quarantäne nach § 4a Absatz 1 Nr. 4 TestV*</td>
                  </tr>
                  <tr>
                    <td class="tg-1lax">{{X5}}</td>
                    <td class="tg-1lax">Besucher und Bewohner vulnerabler Einrichtungen, z.B. Krankenhäuser, Altenheime und Pflegeeinrichtungen nach § 4a Absatz 1 Nr. 5 TestV
                        <br>
                        <label for="">Name u. Anschrift der Einrichtung: <br></label>
                        <input type="text" size="60em;" value="_____________________________________" name="" id="">
                    </td>
                  </tr>
                  <tr>
                    <td class="tg-1lax">{{X6}}</td>
                    <td class="tg-1lax">Menschen mit Behinderung, die Unterstützung über das persönliche Budget erhalten<br> (§ 29 SGB IX) sowie deren Assistenzkräfte nach § 4a Absatz 1 Nr. 8 TestV <br>
                        <label for="">Name der unterstützten Person </label> <input type="text" value="_________________________________________" size="40em;">
                    </td>
                  </tr>
                  <tr>
                    <td class="tg-1lax">{{X7}}</td>
                    <td class="tg-1lax">Pflegende Angehörige und weitere Pflegepersonen im Sinne des § 19 Satz 1 SGB XI nach § 4a Absatz 1 Nr. 9 TestV <br>
                        <label for="">Name der zu pflegenden Person </label> <input type="text" value="__________________________________________" size="40em;">

                    </td>
                  </tr>
                  <tr>
                    <td class="tg-1lax">{{X8}}</td>
                    <td class="tg-1lax">Personen, die mit einer mit dem Coronavirus infizierten Person in demselben Haushalt leben nach § 4a Absatz 1 Nr. 10TestV*
                    </td>
                  </tr>
                
                </tbody>
                </table>

                <style type="text/css">
                    .tg  {border-collapse:collapse;border-spacing:0;}
                    .tg td{font-family:Arial, sans-serif;;
                      overflow:hidden;padding:10px 5px;word-break:normal;}
                    .tg th{font-family:Arial, sans-serif;
                      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
                    .tg .tg-0lax{text-align:left;vertical-align:top; border:none; font-size: smaller;}
                    </style>
                    <table class="tg" style="border: none; margin-top: 1em;">
                    <thead>
                      <tr>
                        <td class="tg-0lax"><u>Hersbruck, <script> document.write(new Date().toLocaleDateString('de-DE')); </script>
                        </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ort, Datum</td>
                        <td class="tg-0lax" style="padding-left: 15em;"></td>
                        <td class="tg-0lax">___________________________<br>Unterschrift der Testperson bzw.<br>des Erziehungsberechtigten<br></td>
                      </tr>
                    </thead>
                    </table>
        </div>
    
    <div>      
        <SPAN style="width: 80em;">__________________________________________________________________________________</SPAN>

        <p>Durch die Teststelle auszufüllen:</p>

        <style type="text/css">
            .tg  {border-collapse:collapse;border-spacing:0; margin: auto;}
            .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
              overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
              font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg .tg-2lax{text-align:left;vertical-align:top; font-size: smaller;}
            </style>
            <table class="tg">
            <thead>
              <tr>
                <th class="tg-2lax">ÖGD-ID (soweit vorhanden)</th>
                <th class="tg-2lax"></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="tg-2lax">dazugehörige Adresse</td>
                <td class="tg-2lax">Teststelle des Landkreises Nürnberger Land</td>
              </tr>
              <tr>
                <td class="tg-2lax">dazugehörige Postleitzahl</td>
                <td class="tg-2lax">91217</td>
              </tr>
              <tr>
                <td class="tg-2lax">dazugehöriger Ort</td>
                <td class="tg-2lax">Hersbruck</td>
              </tr>
            </tbody>
            </table>
    </div>
    <div>
        <br>
        <input type="checkbox"><label for="">Die oben genannte Eigenbeteiligung wurde entrichtet (s. oben)</label>
        <p>Die durch die Testperson vorgenommenen personenbezogenen Angaben wurden seitens der Teststelle auf Richtigkeit überprüft. </p>
        <table class="tg" style="border: none; margin-top: 1em;">
            <thead>
              <tr>
                <td class="tg-0lax"><u>Hersbruck,<script> document.write(new Date().toLocaleDateString('de-DE')); </script> </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbspOrt, Datum</td>
                <td class="tg-0lax" style="padding-left: 15em;"></td>
                <td class="tg-0lax">___________________________<br>Unterschrift der/des Testenden</td>
              </tr>
            </thead>
            </table>

    </div>
</div>
  

 

    <span style="font-size: 0.2em;">*Angaben durch entsprechende Dokumente zu belegen (z.B. amtlicher Lichtbildausweis, ärztliches Attest, Mutterpass, positiver Test, Eintrittskarte, Corona-Warn-App, Testergebnis und Nachweis des Wohnortes).</span>
    <span style="font-size: 0.2em;">**Testungen mit Eigenbeteiligung sind nicht in lokalen Testzentren der Kreisverwaltungsbehörden möglich!</span>
    </div>
   </div>
  

"""

html_tail = '''</body></html>'''