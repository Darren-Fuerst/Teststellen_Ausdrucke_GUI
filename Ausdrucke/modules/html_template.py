
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
        }


        </style>
</head>
<body>'''

html_page_template = '''<div class="page-marker hidden-print" style="word-wrap: break-word; margin-bottom: 20px; margin-left: auto; margin-right: auto; width: 700px; padding-bottom: 15px; border :1px solid black;  box-shadow: 10px 10px 8px #888888;">
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
                <td class="tg-0pky"></td>
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
  </div>'''

html_tail = '''</body></html>'''