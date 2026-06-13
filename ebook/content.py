# -*- coding: utf-8 -*-
"""Inhalt des E-Books 'Herzenssache'. Jedes Kapitel ist HTML."""

BOOK_TITLE = "Herzenssache"
BOOK_SUBTITLE = "Beziehungen verstehen, leben und lieben"
AUTHOR = "Service Alltagshilfe"
LANG = "de"

CSS = """
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.6;
       margin: 5% 6%; color: #2b2b2b; }
h1 { font-family: Helvetica, Arial, sans-serif; color: #c0392b;
     font-size: 1.7em; line-height: 1.25; margin: 0.2em 0 0.8em 0;
     border-bottom: 3px solid #f3b8ac; padding-bottom: 0.3em; }
h2 { font-family: Helvetica, Arial, sans-serif; color: #b8430f;
     font-size: 1.25em; margin-top: 1.6em; }
h3 { font-family: Helvetica, Arial, sans-serif; color: #444;
     font-size: 1.05em; margin-top: 1.2em; }
p { margin: 0.7em 0; text-align: justify; }
.lead { font-size: 1.1em; color: #555; font-style: italic; }
.box { background: #fdf0ec; border-left: 5px solid #e07a5f;
       padding: 0.8em 1em; margin: 1.2em 0; border-radius: 4px; }
.tip { background: #eef7ee; border-left: 5px solid #5a9367;
       padding: 0.8em 1em; margin: 1.2em 0; border-radius: 4px; }
.bsp { background: #eef2fb; border-left: 5px solid #5a7bd6;
       padding: 0.8em 1em; margin: 1.2em 0; border-radius: 4px; }
.box b, .tip b, .bsp b { font-family: Helvetica, Arial, sans-serif; }
ul, ol { margin: 0.6em 0 0.6em 1.2em; }
li { margin: 0.35em 0; }
blockquote { font-style: italic; color: #7a3b2e; border-left: 3px solid #e8c4ba;
       margin: 1.2em 0; padding-left: 1em; }
.center { text-align: center; }
hr { border: none; border-top: 1px solid #e0c9c2; margin: 2em 0; }
.cover-page { text-align: center; }
"""


def tip(t):
    return f'<div class="tip"><b>💚 Tipp:</b> {t}</div>'


def bsp(t):
    return f'<div class="bsp"><b>📖 Beispiel:</b> {t}</div>'


def box(t):
    return f'<div class="box">{t}</div>'


CHAPTERS = []


def add(title, html):
    CHAPTERS.append((title, html))


# ---------------------------------------------------------------------------
add("Vorwort", """
<h1>Vorwort &ndash; Über die Liebe und über dieses Buch</h1>
<p class="lead">Liebe ist das Größte, was wir Menschen einander geben können
&ndash; und gleichzeitig das, woran wir am häufigsten verzweifeln.</p>

<p>In über zwei Jahrzehnten als Paarberater habe ich tausende Geschichten
gehört. Frisch Verliebte, die nicht wussten, wie sie den ersten Schritt
machen. Paare nach dreißig Ehejahren, die sich plötzlich fremd geworden
waren. Singles, die an sich selbst zweifelten. Zwei Frauen, die um die
Anerkennung ihrer Familie kämpften. Männer, die zum ersten Mal in ihrem
Leben weinten, weil sie ihre Kinder nach der Trennung nur noch jedes zweite
Wochenende sahen.</p>

<p>Was ich dabei gelernt habe? Liebe kennt keine Schablone. Sie ist bei
jedem Menschen anders &ndash; und doch folgt sie bestimmten Mustern, die man
verstehen und lernen kann. Genau darum geht es in diesem Buch.</p>

<h2>Für wen ist dieses Buch?</h2>
<p>Für alle. Wirklich für alle. Ob du Single bist und dich fragst, ob du je
den richtigen Menschen findest. Ob du frisch verliebt bist und es richtig
machen willst. Ob du seit Jahrzehnten verheiratet bist und die alte Nähe
vermisst. Ob du Mann und Frau, zwei Männer, zwei Frauen oder einfach zwei
Menschen seid, die einander gefunden haben. Liebe ist Liebe. Dieses Buch
macht keine Unterschiede &ndash; weil das Leben sie auch nicht macht.</p>

<h2>Wie liest man dieses Buch?</h2>
<p>Du musst es nicht von vorne bis hinten lesen. Jedes Kapitel steht für
sich. Blättere zu dem Thema, das dich gerade beschäftigt. Du findest überall
drei wiederkehrende Kästen:</p>
""" + bsp("Hier erzähle ich Geschichten aus der Praxis (alle Namen und Details "
          "habe ich verändert, um die Menschen zu schützen). An ihnen siehst du, "
          "wie das Gelernte im echten Leben aussieht.")
   + tip("Hier findest du konkrete, sofort umsetzbare Ratschläge. Klein genug, "
         "um sie heute noch auszuprobieren.")
   + box("In diesen Kästen fasse ich das Wichtigste zusammen oder gebe dir "
         "eine Übung an die Hand.") + """
<p>Ein letzter Gedanke, bevor wir beginnen: Es gibt keine perfekte Beziehung
und keinen perfekten Menschen. Es gibt nur zwei unperfekte Menschen, die
sich entscheiden, jeden Tag aufs Neue füreinander da zu sein. Das ist nicht
weniger romantisch &ndash; es ist die einzige Romantik, die hält.</p>
<p class="center"><i>Ich wünsche dir von Herzen viel Erkenntnis beim Lesen.</i></p>
""")

# ---------------------------------------------------------------------------
add("Was Liebe wirklich ist", """
<h1>Kapitel 1 &ndash; Was Liebe wirklich ist</h1>
<p class="lead">Wir reden ständig von Liebe. Aber kaum jemand hat je gelernt,
was sie eigentlich ist &ndash; und was sie nicht ist.</p>

<h2>Verliebtheit ist nicht Liebe</h2>
<p>Das ist die wichtigste Unterscheidung des ganzen Buches. Verliebtheit ist
ein Rausch. Biologisch betrachtet überschwemmt das Gehirn den Körper mit
Dopamin, Adrenalin und Serotoninschwankungen &ndash; ein Zustand, der dem
einer leichten Sucht ähnelt. Wir sehen den anderen durch eine rosarote
Brille, übersehen Fehler, können an nichts anderes denken. Das ist
wunderschön. Aber es ist nicht von Dauer, und das ist auch gut so. Niemand
könnte über Jahre in diesem Zustand arbeiten, schlafen oder Steuern
erklären.</p>
<p>Nach etwa sechs Monaten bis drei Jahren ebbt dieser Rausch ab. Viele
Menschen erschrecken dann: &bdquo;Liebe ich ihn nicht mehr?&ldquo; Doch.
Jetzt beginnt erst die eigentliche Liebe &ndash; die Entscheidung, einen
Menschen mit all seinen Ecken und Kanten zu wählen, auch wenn der Rausch
vorbei ist.</p>

""" + bsp("Markus und Lena kamen zu mir, weil &bdquo;das Kribbeln weg&ldquo; war. "
          "Sie hielten das für das Ende. In Wahrheit standen sie an der Schwelle "
          "zur reifen Liebe &ndash; sie wussten es nur nicht. Als sie verstanden, "
          "dass das Abklingen normal ist und nicht ihr Versagen, konnten sie "
          "aufhören, in Panik die Schuld beim anderen zu suchen.") + """

<h2>Die drei Säulen reifer Liebe</h2>
<p>Der Psychologe Robert Sternberg beschrieb Liebe als Dreieck aus drei
Bausteinen. Das ist ein hilfreiches Bild:</p>
<ul>
<li><b>Intimität</b> &ndash; Nähe, Vertrautheit, das Gefühl, sich beim
anderen fallenlassen zu können.</li>
<li><b>Leidenschaft</b> &ndash; Anziehung, Begehren, das Knistern.</li>
<li><b>Bindung / Entscheidung</b> &ndash; die bewusste Wahl, zusammen zu
bleiben und füreinander Verantwortung zu übernehmen.</li>
</ul>
<p>Sind alle drei vorhanden, spricht man von vollkommener Liebe. Aber kein
Paar hat immer alle drei in voller Stärke. Mal überwiegt die Leidenschaft,
mal die Geborgenheit. Das ist normal. Problematisch wird es nur, wenn eine
Säule dauerhaft komplett fehlt.</p>

<h2>Was Liebe nicht ist</h2>
<p>Liebe ist nicht Besitz. Sie ist nicht Eifersucht (&bdquo;Er ist so
eifersüchtig, also liebt er mich richtig&ldquo; &ndash; nein!). Sie ist
nicht das Gefühl, ohne den anderen nicht leben zu können &ndash; das ist
Abhängigkeit. Und Liebe ist nicht die Aufgabe, den anderen zu
&bdquo;reparieren&ldquo; oder zu verändern.</p>

""" + tip("Frag dich nicht: &bdquo;Fühle ich noch Schmetterlinge?&ldquo; "
          "Frag dich: &bdquo;Bin ich neben diesem Menschen ein besserer, ruhigerer, "
          "mutigerer Mensch? Wächst da etwas?&ldquo; Das ist der bessere Kompass.") + """

""" + box("<b>Übung:</b> Schreibe drei Dinge auf, für die du deinem Partner "
          "in der letzten Woche dankbar warst &ndash; ganz konkret, kein großes "
          "&bdquo;weil er so toll ist&ldquo;, sondern &bdquo;weil er mir Kaffee "
          "ans Bett gebracht hat&ldquo;. Dankbarkeit ist der Dünger der Liebe.") + """
""")

# ---------------------------------------------------------------------------
add("Warum wir lieben, wie wir lieben", """
<h1>Kapitel 2 &ndash; Warum wir lieben, wie wir lieben</h1>
<p class="lead">Bevor du verstehst, was zwischen dir und einem anderen
Menschen passiert, musst du verstehen, was in dir selbst passiert.</p>

<h2>Die Bindungstypen</h2>
<p>In den ersten Lebensjahren lernt jeder Mensch unbewusst, wie sicher
Beziehungen sind. Daraus formt sich ein &bdquo;Bindungsstil&ldquo;, der uns
ein Leben lang prägt &ndash; bis wir ihn bewusst verändern. Man unterscheidet
grob drei Muster:</p>

<h3>1. Der sichere Typ</h3>
<p>Fühlt sich mit Nähe wohl, kann aber auch alleine sein. Vertraut, ohne zu
klammern. Spricht Probleme an, ohne zu dramatisieren. Etwa die Hälfte aller
Menschen ist überwiegend sicher gebunden &ndash; und wer es nicht ist, kann
es lernen.</p>

<h3>2. Der ängstliche Typ</h3>
<p>Sehnt sich nach Nähe, hat aber ständig Angst, verlassen zu werden. Liest
in jeder kurzen Antwort eine Katastrophe (&bdquo;Warum schreibt sie nur
&sbquo;ok&lsquo;? Ist sie sauer?&ldquo;). Braucht viel Bestätigung. Klammert
in Stressphasen.</p>

<h3>3. Der vermeidende Typ</h3>
<p>Wirkt unabhängig und stark, fühlt sich aber von zu viel Nähe schnell
eingeengt. Zieht sich bei Konflikten zurück, braucht Freiraum, tut sich
schwer, über Gefühle zu reden.</p>

""" + bsp("Das klassische, schmerzhafte Paar: Sie ist ängstlich, er ist "
          "vermeidend. Je mehr sie Nähe sucht, desto mehr zieht er sich zurück. "
          "Je mehr er sich zurückzieht, desto panischer wird sie. Ein Teufelskreis. "
          "Beide tun nicht etwas Böses &ndash; sie folgen nur ihren alten Mustern. "
          "Sobald sie das erkannten, konnten Sandra und Tobias aufhören, einander "
          "als Feind zu sehen.") + """

<h2>Warum das so wichtig ist</h2>
<p>Wenn du deinen eigenen Typ kennst, hörst du auf, deine Reaktionen für
&bdquo;die Wahrheit&ldquo; zu halten. Die ängstliche Frau lernt: &bdquo;Mein
Alarm bedeutet nicht, dass wirklich Gefahr droht.&ldquo; Der vermeidende Mann
lernt: &bdquo;Mein Drang wegzulaufen ist alter Selbstschutz, kein
Liebesentzug.&ldquo;</p>

""" + tip("Finde heraus, welcher Typ du tendenziell bist (es gibt gute "
          "Online-Tests, such nach &bdquo;Bindungsstil Test&ldquo;). Sprich mit "
          "deinem Partner darüber. Allein der Satz &bdquo;Wenn ich mich zurückziehe, "
          "lehne ich dich nicht ab &ndash; ich brauche kurz Luft und komme "
          "wieder&ldquo; kann eine Beziehung retten.") + """

<h2>Die fünf Sprachen der Liebe</h2>
<p>Menschen drücken Liebe unterschiedlich aus und nehmen sie unterschiedlich
wahr. Gary Chapman beschrieb fünf &bdquo;Liebessprachen&ldquo;:</p>
<ol>
<li><b>Lob und Anerkennung</b> &ndash; liebevolle Worte.</li>
<li><b>Zweisamkeit</b> &ndash; ungeteilte gemeinsame Zeit.</li>
<li><b>Geschenke</b> &ndash; kleine Aufmerksamkeiten.</li>
<li><b>Hilfsbereitschaft</b> &ndash; dem anderen etwas abnehmen.</li>
<li><b>Zärtlichkeit</b> &ndash; Berührung, Körperkontakt.</li>
</ol>
""" + bsp("Eine Frau brachte ihrem Mann täglich seine Lieblingsschokolade mit "
          "und fühlte sich ungeliebt, weil er &bdquo;nie etwas tat&ldquo;. Er "
          "wiederum reparierte ständig Dinge im Haus &ndash; seine Art, Liebe zu "
          "zeigen. Beide liebten sich sehr. Sie sprachen nur verschiedene Sprachen "
          "und hörten die des anderen nicht.") + """
""" + tip("Frag deinen Partner direkt: &bdquo;Wann fühlst du dich von mir am "
          "meisten geliebt?&ldquo; Und dann gib ihm genau das &ndash; in SEINER "
          "Sprache, nicht in deiner.") + """
""")

# ---------------------------------------------------------------------------
add("Single sein", """
<h1>Kapitel 3 &ndash; Single sein: allein, aber nicht einsam</h1>
<p class="lead">Single zu sein ist kein Wartezimmer, in dem das Leben erst
beginnt, sobald jemand kommt. Es ist ein vollwertiges Leben.</p>

<h2>Der gefährlichste Glaubenssatz</h2>
<p>&bdquo;Ich bin erst vollständig, wenn ich jemanden habe.&ldquo; Dieser Satz
hat schon mehr Lebensglück zerstört als jede Trennung. Denn er macht dich
abhängig und verzweifelt &ndash; und Verzweiflung ist das Unattraktivste
überhaupt. Menschen spüren, ob du aus einem Mangel heraus suchst oder aus
einer Fülle heraus teilst.</p>

""" + bsp("Petra, 52, frisch geschieden, sagte mir: &bdquo;Ich kann nicht "
          "allein sein.&ldquo; Ich schickte sie nicht auf Partnersuche, sondern "
          "bat sie, drei Monate lang bewusst Dinge nur für sich zu tun: ein Kurs, "
          "ein Wochenendtrip allein, ein altes Hobby. Nach drei Monaten kam sie "
          "zurück und sagte: &bdquo;Ich habe gemerkt, dass ich mich selbst ganz "
          "gut leiden kann.&ldquo; Ein halbes Jahr später lernte sie jemanden "
          "kennen &ndash; aus Stärke, nicht aus Not.") + """

<h2>Die Single-Zeit sinnvoll nutzen</h2>
<ul>
<li><b>Lerne dich kennen.</b> Was willst du im Leben wirklich? Was sind deine
Werte? Wer das nicht weiß, sucht in jeder Beziehung den anderen als Antwort
&ndash; und wird enttäuscht.</li>
<li><b>Baue ein Leben, das dir gefällt.</b> Freundschaften, Hobbys, Arbeit,
die Sinn stiftet. Ein erfülltes Single-Leben ist die beste Grundlage für eine
gesunde Partnerschaft.</li>
<li><b>Heile alte Wunden.</b> Wer unverarbeitete Verletzungen mit in die
nächste Beziehung trägt, wiederholt oft dieselben Muster.</li>
</ul>

<h2>Einsamkeit ist nicht gleich Alleinsein</h2>
<p>Man kann tief einsam sein mitten in einer Ehe &ndash; und vollkommen
zufrieden allein. Einsamkeit ist ein Gefühl der Verbindungslosigkeit, nicht
der Mangel an einem Partner. Wenn dich Einsamkeit quält, brauchst du nicht
zwingend einen Partner, sondern Verbindung: zu Freunden, zur Familie, zu einer
Gemeinschaft, zu dir selbst.</p>

""" + tip("Mach diese Woche eine &bdquo;Verabredung mit dir selbst&ldquo;: Geh "
          "allein essen oder ins Kino. Klingt seltsam, ist aber Gold wert. Wer "
          "die eigene Gesellschaft genießen kann, wird in keiner Beziehung "
          "klammern müssen.") + """

<h2>Wieder bereit für Liebe?</h2>
<p>Du musst nicht &bdquo;perfekt geheilt&ldquo; sein, bevor du wieder liebst
&ndash; das wäre eine Ausrede. Aber drei Fragen helfen:</p>
<ol>
<li>Suche ich einen Partner, um eine Lücke zu füllen, oder um mein volles
Leben zu teilen?</li>
<li>Kann ich über meine letzte Beziehung sprechen, ohne nur in Wut oder
Trauer zu versinken?</li>
<li>Weiß ich, was ich diesmal anders machen will?</li>
</ol>
""" + box("<b>Merksatz:</b> Du bist kein halber Mensch auf der Suche nach deiner "
          "anderen Hälfte. Du bist ein ganzer Mensch, der einen anderen ganzen "
          "Menschen sucht, um gemeinsam mehr zu sein.") + """
""")

# ---------------------------------------------------------------------------
add("Partnersuche und Dating", """
<h1>Kapitel 4 &ndash; Partnersuche und Dating</h1>
<p class="lead">Den richtigen Menschen zu finden ist kein Glücksspiel allein.
Vieles lässt sich klüger angehen.</p>

<h2>Wer passt zu mir &ndash; und wer nicht?</h2>
<p>Viele suchen nach einer Liste von Äußerlichkeiten: Größe, Beruf, Aussehen.
Doch was Beziehungen langfristig trägt, sind gemeinsame <b>Werte</b> und
<b>Lebensziele</b>. Will jemand Kinder, du aber nicht? Ist Treue für beide
gleich wichtig? Wie steht ihr zu Geld, Familie, Freiheit? Solche Fragen
entscheiden über Jahrzehnte &ndash; nicht die Haarfarbe.</p>

""" + tip("Erstelle zwei Listen: &bdquo;Das muss sein&ldquo; (höchstens 5 "
          "echte Werte, keine Äußerlichkeiten) und &bdquo;Das geht gar "
          "nicht&ldquo; (deine Grenzen). Alles andere ist Verhandlungssache. "
          "Wer 30 Kriterien hat, findet niemanden &ndash; oder den Falschen.") + """

<h2>Online-Dating &ndash; Chance und Falle</h2>
<p>Apps sind heute der häufigste Weg, sich kennenzulernen &ndash; in jedem
Alter. Sie sind ein Werkzeug, nicht mehr und nicht weniger. Ein paar
Wahrheiten:</p>
<ul>
<li><b>Das Profil:</b> Echte, aktuelle Fotos (auch ein Lächeln!), ein Text,
der zeigt wer du bist, nicht eine Liste von Forderungen. Humor zieht.</li>
<li><b>Das Wischen macht süchtig:</b> Die endlose Auswahl gaukelt vor, der
&bdquo;Bessere&ldquo; sei nur einen Wisch entfernt. Das verhindert echtes
Einlassen. Triff dich lieber früher in echt als ewig zu schreiben.</li>
<li><b>Sicherheit zuerst:</b> Erstes Treffen an einem öffentlichen Ort.
Jemandem Bescheid geben, wo du bist. Auf Geldforderungen NIEMALS eingehen
(Stichwort Romance Scam &ndash; dazu gleich mehr).</li>
</ul>

""" + box("<b>Achtung Liebesbetrug (Romance Scam):</b> Wenn jemand schnell von "
          "großer Liebe spricht, aber nie zum Videocall oder Treffen bereit ist "
          "und irgendwann Geld braucht (Notlage, Zoll, Krankheit) &ndash; brich "
          "den Kontakt ab. Das ist Betrug, kein Pech. Das gilt besonders, aber "
          "nicht nur, für ältere Suchende.") + """

<h2>Das erste Date</h2>
<p>Vergiss die Idee, dich &bdquo;verkaufen&ldquo; zu müssen. Ein Date ist
kein Vorstellungsgespräch, sondern ein gegenseitiges Kennenlernen &ndash; du
prüfst auch, ob ER/SIE zu dir passt.</p>
""" + bsp("Ein Klient war vor jedem Date so nervös, dass er ununterbrochen "
          "redete. Mein Rat: &bdquo;Stell drei echte Fragen und hör wirklich "
          "zu.&ldquo; Beim nächsten Date sagte die Frau am Ende: &bdquo;Mit dir "
          "kann man so schön reden.&ldquo; Er hatte fast nichts über sich "
          "erzählt &ndash; aber echtes Interesse gezeigt. Das ist anziehender "
          "als jede Selbstdarstellung.") + """

<h3>Gute Fragen fürs Kennenlernen</h3>
<ul>
<li>&bdquo;Was begeistert dich gerade?&ldquo;</li>
<li>&bdquo;Wie sieht für dich ein perfekter freier Tag aus?&ldquo;</li>
<li>&bdquo;Was ist dir bei Menschen wichtig?&ldquo;</li>
</ul>

""" + tip("Achte beim Date weniger darauf, was jemand sagt, und mehr darauf, "
          "WIE er sich verhält: Ist er freundlich zur Kellnerin? Hört er zu? "
          "Respektiert er ein Nein? Charakter zeigt sich im Kleinen.") + """

<h2>Wenn der Funke nicht überspringt</h2>
<p>Manchmal passt es einfach nicht &ndash; das ist niemandes Schuld. Sag
freundlich und ehrlich ab, statt zu &bdquo;ghosten&ldquo; (sich kommentarlos
in Luft auflösen). Eine kurze, ehrliche Nachricht ist Anstand: &bdquo;Ich
fand den Abend nett, spüre aber nicht das Romantische. Ich wünsche dir von
Herzen alles Gute.&ldquo;</p>
""")

# ---------------------------------------------------------------------------
add("Die Phasen einer Beziehung", """
<h1>Kapitel 5 &ndash; Die Phasen einer Beziehung</h1>
<p class="lead">Jede Liebe durchläuft Phasen. Wer sie kennt, gerät nicht in
Panik, wenn sich etwas verändert &ndash; denn Veränderung ist normal.</p>

<h2>Phase 1: Verliebtheit (der Höhenflug)</h2>
<p>Alles ist rosig, der andere ist perfekt. Genieße sie! Aber triff in dieser
Phase keine unumkehrbaren Entscheidungen, die dein ganzes Leben umkrempeln
&ndash; das Gehirn ist im Ausnahmezustand.</p>

<h2>Phase 2: Die Ernüchterung (der erste Streit)</h2>
<p>Die rosarote Brille fällt. Plötzlich nerven Marotten, die vorher süß
waren. Viele Paare erschrecken hier. Dabei ist das ein gutes Zeichen: Ihr
seht euch jetzt als echte Menschen. Hier entscheidet sich, ob aus
Verliebtheit Liebe wird.</p>

""" + bsp("Ein junges Paar trennte sich nach genau diesem Punkt &ndash; und "
          "dann wieder beim nächsten Partner, und beim übernächsten. Sie hielten "
          "das Ende der Verliebtheit jedes Mal für das Ende der Liebe. Erst als "
          "sie begriffen, dass nach dem Rausch die Arbeit (und die tiefere "
          "Belohnung) beginnt, konnten sie bleiben.") + """

<h2>Phase 3: Die Aushandlung</h2>
<p>Wer macht was? Wie viel Nähe, wie viel Freiheit? Wie verbringen wir die
Feiertage? Hier werden die Regeln des gemeinsamen Lebens ausgehandelt. Das
kann anstrengend sein, ist aber gesund. Paare, die nie streiten, kehren oft
nur Probleme unter den Teppich.</p>

<h2>Phase 4: Stabilität und tiefe Bindung</h2>
<p>Ihr kennt euch, vertraut euch, seid ein eingespieltes Team. Die Gefahr
hier: Routine und Selbstverständlichkeit. Man hört auf, sich zu bemühen. Dazu
mehr im Kapitel über Langzeitbeziehungen.</p>

<h2>Phase 5: Erneuerung</h2>
<p>Gute Langzeitpaare durchlaufen die Phasen nicht einmal, sondern immer
wieder in kleinen Zyklen. Nach Krisen finden sie zu neuer, tieferer Nähe. Die
Liebe mit 60 ist eine andere als mit 25 &ndash; oft eine reichere.</p>

""" + tip("Frag dich bei jeder Veränderung nicht &bdquo;Ist die Liebe "
          "vorbei?&ldquo;, sondern &bdquo;In welcher Phase stecken wir gerade, "
          "und was braucht diese Phase von uns?&ldquo;") + """

""" + box("<b>Wichtig:</b> Krisen sind keine Betriebsstörung der Liebe &ndash; "
          "sie sind ihr Wachstumsmotor. Fast jedes starke Paar, das ich kenne, "
          "ist mindestens einmal fast zerbrochen und daran gewachsen.") + """
""")

# ---------------------------------------------------------------------------
add("Kommunikation", """
<h1>Kapitel 6 &ndash; Kommunikation: das Herzstück</h1>
<p class="lead">Die meisten Paare, die zu mir kommen, haben kein
Liebesproblem. Sie haben ein Kommunikationsproblem.</p>

<h2>Die vier Reiter der Apokalypse</h2>
<p>Der Forscher John Gottman kann mit über 90% Treffsicherheit vorhersagen,
ob ein Paar sich trennt &ndash; allein daran, wie es streitet. Vier
Verhaltensweisen sind besonders zerstörerisch:</p>
<ol>
<li><b>Kritik</b> (Angriff auf die Person statt auf das Verhalten): &bdquo;Du
bist so egoistisch&ldquo; statt &bdquo;Ich war traurig, dass du ohne mich
gegangen bist.&ldquo;</li>
<li><b>Verachtung</b> (Augenrollen, Spott, Herabsetzung) &ndash; der
gefährlichste Reiter. Verachtung ist Gift.</li>
<li><b>Rechtfertigung / Abwehr</b> (&bdquo;Ich bin doch gar nicht
schuld!&ldquo;).</li>
<li><b>Mauern</b> (dichtmachen, schweigen, weggehen).</li>
</ol>

""" + bsp("Ein Paar, beide Akademiker, hochintelligent &ndash; und doch redeten "
          "sie miteinander in Verachtung. Sie rollte mit den Augen, er machte sie "
          "vor den Kindern lächerlich. Wir arbeiteten Monate nur an diesem einen "
          "Punkt: Respekt im Ton. Als die Verachtung verschwand, kam die "
          "Zuneigung von selbst zurück.") + """

<h2>Die Ich-Botschaft</h2>
<p>Die wichtigste Technik überhaupt. Statt mit &bdquo;Du&ldquo; anzugreifen,
sprich von dir:</p>
<ul>
<li>Statt: &bdquo;Du hörst mir nie zu!&ldquo;</li>
<li>Sondern: &bdquo;Ich fühle mich übersehen, wenn ich rede und du aufs Handy
schaust. Ich wünsche mir deine Aufmerksamkeit.&ldquo;</li>
</ul>
<p>Das Muster: <i>Wenn (konkrete Situation) &ndash; dann fühle ich (Gefühl)
&ndash; weil (Bedürfnis) &ndash; ich wünsche mir (Bitte).</i> Der andere muss
sich nicht verteidigen und kann zuhören.</p>

<h2>Aktives Zuhören</h2>
<p>Zuhören heißt nicht, in der Pause schon die Gegenrede vorzubereiten. Es
heißt, wirklich verstehen zu wollen. Eine einfache, fast magische Technik:
das Gehörte in eigenen Worten wiederholen.</p>
""" + bsp("&bdquo;Du bist also enttäuscht, weil du dir an deinem Geburtstag "
          "mehr Aufmerksamkeit von mir gewünscht hättest &ndash; hab ich das "
          "richtig verstanden?&ldquo; Allein dieser Satz lässt den anderen sich "
          "gesehen fühlen. Oft löst sich der halbe Streit dadurch in Luft auf.") + """

""" + tip("Vereinbart ein &bdquo;Wochengespräch&ldquo;: 20 Minuten, einmal pro "
          "Woche, ohne Handy. Jeder beantwortet: Was lief gut bei uns? Was hat "
          "mich beschäftigt? Was wünsche ich mir für die nächste Woche? Das "
          "verhindert, dass sich Kleinkram zu einer Bombe ansammelt.") + """

<h2>Der richtige Zeitpunkt</h2>
<p>Schwierige Gespräche nie zwischen Tür und Angel, nicht hungrig, müde oder
betrunken. Es gibt das schöne englische Wort &bdquo;HALT&ldquo;: Sprich keine
Konflikte an, wenn du <b>H</b>ungry, <b>A</b>ngry, <b>L</b>onely oder
<b>T</b>ired bist. Erst essen, beruhigen, ausruhen &ndash; dann reden.</p>
""" + box("<b>Übung:</b> Formuliere den nächsten Vorwurf, der dir auf der Zunge "
          "liegt, einmal komplett als Ich-Botschaft um, bevor du ihn aussprichst. "
          "Schreib ihn notfalls erst auf.") + """
""")

# ---------------------------------------------------------------------------
add("Streiten will gelernt sein", """
<h1>Kapitel 7 &ndash; Streiten will gelernt sein</h1>
<p class="lead">Es geht nicht darum, ob ihr streitet, sondern WIE. Gut
gestrittene Konflikte machen eine Beziehung stärker.</p>

<h2>Das Ziel ist nicht zu gewinnen</h2>
<p>Der größte Denkfehler: Im Streit gegen den Partner gewinnen zu wollen.
Wenn du gewinnst, verliert der Mensch, den du liebst &ndash; und damit
verliert ihr beide. Das Ziel ist nicht ein Sieger, sondern eine Lösung, mit
der ihr beide leben könnt. Ihr sitzt im selben Boot, das Problem ist der
Gegner, nicht der andere.</p>

""" + bsp("Ein Ehepaar stritt seit Jahren über die Zahnpastatube. Klingt "
          "lächerlich? Es ging nie um Zahnpasta. Es ging darum, dass sie sich "
          "nicht respektiert und nicht gehört fühlte. Als das auf dem Tisch lag, "
          "war die Tube plötzlich egal.") + """

<h2>Die Eskalations-Bremse</h2>
<p>Im hitzigen Streit wird das logische Denken vom Stress regelrecht
abgeschaltet (&bdquo;Flooding&ldquo;). Der Puls steigt über 100, man sagt
Dinge, die man nicht meint. Dann hilft nur eins: Pause.</p>
""" + tip("Vereinbart ein Stopp-Signal (ein Wort, eine Geste). Wenn einer es "
          "gibt, macht ihr 20&ndash;30 Minuten Pause &ndash; aber mit dem "
          "ausdrücklichen Versprechen, danach weiterzureden. Wichtig: In der "
          "Pause NICHT weiter grübeln und Munition sammeln, sondern wirklich "
          "runterkommen (kurz rausgehen, atmen).") + """

<h2>Fair-Streiten-Regeln</h2>
<ul>
<li>Beim aktuellen Thema bleiben &ndash; keine alten Sünden ausgraben
(&bdquo;Und vor drei Jahren hast du auch&hellip;&ldquo;).</li>
<li>Keine Verallgemeinerungen: &bdquo;immer&ldquo; und &bdquo;nie&ldquo; sind
verboten.</li>
<li>Keine Beleidigungen, keine Drohungen mit Trennung als Druckmittel.</li>
<li>Nicht vor den Kindern und nicht vor anderen.</li>
<li>Ein Thema nach dem anderen.</li>
</ul>

<h2>Sich entschuldigen &ndash; richtig</h2>
<p>Eine echte Entschuldigung enthält kein &bdquo;aber&ldquo;. &bdquo;Es tut
mir leid, aber du hast&hellip;&ldquo; ist keine Entschuldigung, sondern ein
versteckter Angriff. Eine echte lautet: &bdquo;Es tut mir leid. Ich sehe,
dass ich dich verletzt habe. Das wollte ich nicht.&ldquo;</p>

<h2>Versöhnen will auch gelernt sein</h2>
<p>Nach dem Streit ist vor der Nähe. Gönnt euch eine Geste der Versöhnung
&ndash; eine Umarmung, ein ehrliches &bdquo;Schön, dass wir das geklärt
haben.&ldquo; Paare, die sich gut versöhnen, überstehen fast alles.</p>

""" + box("<b>Merksatz:</b> Frag dich im Streit: &bdquo;Will ich Recht haben "
          "oder will ich glücklich sein?&ldquo; Beides geht selten gleichzeitig.") + """
""")

# ---------------------------------------------------------------------------
add("Vertrauen, Eifersucht und Treue", """
<h1>Kapitel 8 &ndash; Vertrauen, Eifersucht und Treue</h1>
<p class="lead">Vertrauen ist das Fundament. Ohne es ist jede Beziehung ein
Haus auf Sand.</p>

<h2>Vertrauen entsteht durch Verlässlichkeit</h2>
<p>Vertrauen ist kein Geschenk und kein Glücksfall &ndash; es wächst aus
tausend kleinen Momenten, in denen jemand tut, was er sagt. Wer pünktlich ist,
zu seinem Wort steht, ehrlich auch bei Kleinigkeiten ist, baut ein Konto auf,
von dem das Paar in Krisen zehrt.</p>

<h2>Eifersucht verstehen</h2>
<p>Ein bisschen Eifersucht ist menschlich. Aber krankhafte Eifersucht hat
selten mit dem Partner zu tun &ndash; fast immer mit eigenen Ängsten und
geringem Selbstwert. Sie kontrolliert, durchsucht Handys, verbietet Kontakte.
Das ist keine Liebe, das ist Angst, die zur Kontrolle wird &ndash; und sie
erstickt genau die Beziehung, die sie schützen will.</p>

""" + bsp("Ein Mann kontrollierte das Handy seiner Frau täglich. Sie hatte nie "
          "etwas getan. Doch je mehr er kontrollierte, desto mehr zog sie sich "
          "zurück &ndash; und desto misstrauischer wurde er. In der Beratung "
          "stellte sich heraus: Sein Vater hatte die Mutter betrogen. Er bekämpfte "
          "ein altes Trauma im falschen Menschen. Als er das erkannte, konnte er "
          "beginnen, an sich statt an ihr zu arbeiten.") + """

""" + tip("Wenn dich Eifersucht quält, frag dich ehrlich: &bdquo;Gibt es "
          "echte, konkrete Hinweise &ndash; oder ist das mein altes Gefühl, "
          "nicht genug zu sein?&ldquo; Sprich über die ANGST ("
          "&bdquo;Ich habe Angst, dich zu verlieren&ldquo;), nicht über "
          "Verdächtigungen (&bdquo;Mit wem schreibst du da?&ldquo;).") + """

<h2>Untreue &ndash; und was wirklich dahintersteckt</h2>
<p>Affären sind selten nur über Sex. Meist fehlt etwas: Aufmerksamkeit,
Anerkennung, das Gefühl, begehrt zu sein, Nähe, manchmal auch nur der Kitzel,
sich lebendig zu fühlen. Das ist keine Entschuldigung &ndash; Untreue ist ein
Vertrauensbruch, für den der Untreue die Verantwortung trägt. Aber wer die
tiefere Ursache versteht, kann (wenn beide wollen) daran arbeiten.</p>

<h2>Kann man nach einem Seitensprung weitermachen?</h2>
<p>Ja &ndash; viele Paare kommen sogar gestärkt heraus. Aber nur unter
Bedingungen:</p>
<ul>
<li>Die Affäre ist wirklich beendet, vollständig.</li>
<li>Der Untreue zeigt echte Reue, keine Ausreden, übernimmt Verantwortung.</li>
<li>Er/sie ist bereit, eine Zeit lang Transparenz zu geben, um Vertrauen
wieder aufzubauen.</li>
<li>Beide wollen verstehen, was gefehlt hat &ndash; nicht um Schuld
abzuwälzen, sondern um die Beziehung neu zu bauen.</li>
</ul>
""" + box("<b>Wichtig für den Betrogenen:</b> Du darfst wütend und verletzt sein, "
          "so lange du es brauchst. Aber endloses Bestrafen heilt nicht. "
          "Irgendwann steht die Entscheidung an: wirklich verzeihen und neu "
          "beginnen &ndash; oder gehen. Beides ist ehrenhaft. Nur im Dazwischen, "
          "in der ewigen Bestrafung, leiden beide.") + """

<h2>Vertrauen wieder aufbauen</h2>
<p>Es braucht Zeit &ndash; oft Monate, manchmal Jahre. Geduld auf beiden
Seiten. Der eine muss Verlässlichkeit beweisen, der andere muss irgendwann
bereit sein, den ersten Schritt zurück ins Vertrauen zu wagen. Eine
Paartherapie ist hier oft Gold wert.</p>
""")

# ---------------------------------------------------------------------------
add("Nähe, Zärtlichkeit und Sexualität", """
<h1>Kapitel 9 &ndash; Nähe, Zärtlichkeit und Sexualität</h1>
<p class="lead">Körperliche Nähe ist die Sprache, die keine Worte braucht
&ndash; und doch reden Paare über kaum etwas so ungern.</p>

<h2>Sex ist ein Spiegel der Beziehung</h2>
<p>Wenn es im Bett nicht läuft, liegt das Problem oft außerhalb des
Schlafzimmers: ungelöste Konflikte, Stress, fehlende emotionale Nähe,
Erschöpfung. Begehren braucht Sicherheit UND Spannung &ndash; ein feines
Gleichgewicht.</p>

<h2>Lust ist nicht bei allen gleich</h2>
<p>Es gibt &bdquo;spontane&ldquo; Lust (Verlangen kommt aus dem Nichts) und
&bdquo;reaktive&ldquo; Lust (Verlangen entsteht erst durch Berührung und
Nähe). Viele Paare glauben fälschlich, etwas stimme nicht, weil einer selten
von sich aus Lust verspürt. Dabei ist reaktive Lust völlig normal &ndash;
besonders in Langzeitbeziehungen und oft (nicht immer) bei Frauen.</p>

""" + bsp("Ein Paar war überzeugt, ihre Ehe sei kaputt, weil sie &bdquo;nie "
          "Lust&ldquo; hatte. In Wahrheit hatte sie reaktive Lust: Sobald sie "
          "sich auf Nähe einließ, stellte sich das Verlangen ein. Sie warteten "
          "nur beide auf einen spontanen Funken, der bei ihr selten von allein "
          "kam. Die Lösung war nicht weniger Liebe, sondern mehr bewusste "
          "Zärtlichkeit ohne Erwartungsdruck.") + """

<h2>Über Sex reden lernen</h2>
<p>Niemand kann Gedanken lesen. Das, was du dir wünschst, wird dein Partner
nur erfüllen, wenn er es weiß. Sprich liebevoll und konkret &ndash; nicht als
Kritik (&bdquo;Du machst das immer falsch&ldquo;), sondern als Einladung
(&bdquo;Ich mag es besonders, wenn du&hellip;&ldquo;).</p>

""" + tip("Redet über Wünsche AUSSERHALB des Schlafzimmers, in entspannter "
          "Atmosphäre &ndash; nicht im Moment selbst, wo jede Bemerkung schnell "
          "verletzt. Ein Spaziergang ist ein guter Ort für so ein Gespräch.") + """

<h2>Wenn die Lust eingeschlafen ist</h2>
<p>In langen Beziehungen wird Sex oft seltener &ndash; das ist normal und
kein Drama. Problematisch wird es nur, wenn ein Partner darunter leidet und
nicht darüber gesprochen wird. Zärtlichkeit muss nicht immer in Sex münden.
Oft ist es das Kuscheln, das Händchenhalten, die Umarmung von hinten in der
Küche, das die Verbindung lebendig hält.</p>

""" + box("<b>Übung:</b> Berührt euch eine Woche lang bewusst jeden Tag "
          "mindestens einmal liebevoll &ndash; ganz ohne dass es zu mehr führen "
          "MUSS. Diese Entkopplung nimmt den Druck und lässt echtes Begehren oft "
          "von selbst zurückkehren.") + """

<h2>Unterschiedliches Verlangen</h2>
<p>Fast nie haben zwei Menschen exakt gleich viel Lust. Das ist kein Defekt.
Es geht um respektvollen Umgang: Der mit mehr Verlangen darf keinen Druck
ausüben, der mit weniger darf sich nicht völlig verweigern. Es braucht
Kompromisse, Zärtlichkeit und Verständnis &ndash; auf beiden Seiten.</p>
""" + tip("Wenn körperliche Probleme (Schmerzen, Erektionsstörungen, "
          "Wechseljahre, Medikamente) eine Rolle spielen: Schämt euch nicht, "
          "ärztliche Hilfe zu suchen. Vieles ist gut behandelbar.") + """
""")

# ---------------------------------------------------------------------------
add("Gleichgeschlechtliche und queere Beziehungen", """
<h1>Kapitel 10 &ndash; Gleichgeschlechtliche und queere Beziehungen</h1>
<p class="lead">Liebe ist Liebe. Alles in diesem Buch gilt für jede
Beziehung. Und doch gibt es Erfahrungen, die queere Paare besonders
betreffen.</p>

<h2>Dieselbe Liebe, dieselben Themen</h2>
<p>Kommunikation, Vertrauen, Streit, Nähe, Eifersucht &ndash; all das
funktioniert bei zwei Frauen, zwei Männern oder nicht-binären Menschen genauso
wie bei allen anderen. Lass dir niemals einreden, deine Liebe sei
&bdquo;anders&ldquo; oder weniger wert. Sie ist es nicht.</p>

<h2>Das Coming-out &ndash; ein eigener Weg</h2>
<p>Viele queere Menschen tragen die Erfahrung in sich, sich erst zu sich
selbst und dann zur Welt bekennen zu müssen. Das prägt. In einer Beziehung
können zwei Menschen an ganz unterschiedlichen Punkten dieses Weges stehen:
Der eine lebt offen, der andere ist bei der Familie noch nicht geoutet.</p>

""" + bsp("Zwei Männer, seit zwei Jahren zusammen. Der eine wollte zu "
          "Familienfeiern als Paar auftreten, der andere war bei seinen streng "
          "religiösen Eltern noch nicht geoutet und hatte echte Angst. Das war "
          "kein Mangel an Liebe &ndash; es waren zwei Realitäten. Die Lösung lag "
          "nicht in Druck, sondern in Geduld und dem gemeinsamen Festlegen eines "
          "Tempos, das beide tragen konnten.") + """

""" + tip("Wenn ihr an unterschiedlichen Punkten des Coming-outs steht: "
          "Respektiert das Tempo des anderen, aber redet offen über die "
          "Gefühle, die das auslöst. Niemand sollte sich verstecken müssen "
          "&ndash; und niemand sollte zu etwas gedrängt werden, wofür er noch "
          "nicht bereit ist. Findet einen Plan, der beide Bedürfnisse ehrt.") + """

<h2>Umgang mit Ablehnung von außen</h2>
<p>Auch heute erleben queere Paare noch Blicke, dumme Sprüche, manchmal
Ablehnung der eigenen Familie. Das ist eine zusätzliche Last, die Paare
gemeinsam tragen müssen. Wichtig ist, dass das Paar nach innen ein sicherer
Hafen bleibt &ndash; ein Ort, an dem beide bedingungslos angenommen sind.</p>

""" + box("<b>Wichtig:</b> Sucht euch ein unterstützendes Umfeld &ndash; "
          "Freunde, Communities, Beratungsstellen (z.&nbsp;B. lokale "
          "queere Zentren). Eine Beziehung kann nicht die einzige Quelle von "
          "Akzeptanz sein. Ein Netz aus Menschen, die euch feiern, entlastet die "
          "Partnerschaft enorm.") + """

<h2>Eigene Lebensmodelle</h2>
<p>Queere Paare sind oft freier von alten Rollenklischees (&bdquo;Wer ist der
Mann, wer die Frau?&ldquo; &ndash; eine Frage, die schlicht keinen Sinn
ergibt). Diese Freiheit ist eine Chance: Ihr könnt eure Rollen, eure
Aufgabenteilung, euer Modell von Treue und Familie ganz bewusst selbst
gestalten, statt Vorlagen zu übernehmen. Nutzt sie &ndash; und sprecht
ausdrücklich darüber, was ihr wollt.</p>

<h2>Familienplanung</h2>
<p>Kinderwunsch ist in queeren Beziehungen genauso da &ndash; nur die Wege
sind andere (Adoption, Pflegekinder, Co-Elternschaft, medizinische
Möglichkeiten). Das erfordert Planung und manchmal einen langen Atem. Wichtig
ist, dass beide denselben Wunsch und dasselbe Bild von Familie teilen.</p>

<p class="center"><i>Eure Liebe braucht keine Rechtfertigung. Sie braucht nur
Pflege &ndash; wie jede Liebe.</i></p>
""")

# ---------------------------------------------------------------------------
add("Verheiratet und Langzeitbeziehungen", """
<h1>Kapitel 11 &ndash; Wie Liebe über Jahrzehnte bleibt</h1>
<p class="lead">Verliebt sein kann jeder. Eine Liebe über Jahrzehnte lebendig
zu halten &ndash; das ist die wahre Kunst.</p>

<h2>Der größte Feind: Selbstverständlichkeit</h2>
<p>Am Anfang strengen wir uns an: Wir hören zu, machen Komplimente, planen
Überraschungen. Mit den Jahren schleicht sich das Gefühl ein, der andere sei
&bdquo;sicher&ldquo; &ndash; und wir hören auf, uns zu bemühen. Genau hier
beginnt das langsame Auseinanderleben. Niemand ist je &bdquo;sicher&ldquo;.
Liebe ist ein Garten, der täglich gegossen werden muss.</p>

""" + bsp("Ein Paar, 35 Jahre verheiratet, saß bei mir und sagte: &bdquo;Wir "
          "sind nur noch Mitbewohner.&ldquo; Sie redeten nur noch über "
          "Organisatorisches &ndash; Müll, Termine, Kinder. Ich gab ihnen eine "
          "simple Aufgabe: jeden Abend zehn Minuten reden, aber NICHT über "
          "Aufgaben &ndash; nur über sich, über Gedanken, über den Tag. Nach "
          "sechs Wochen sagten sie, sie hätten sich &bdquo;wieder kennengelernt&ldquo;.") + """

<h2>Rituale, die Liebe am Leben halten</h2>
<ul>
<li><b>Das Begrüßungs- und Abschiedsritual:</b> Sich morgens und abends
bewusst (mit Kuss, Umarmung) verabschieden und begrüßen &ndash; nicht im
Vorbeigehen.</li>
<li><b>Der wöchentliche Date-Abend:</b> Ja, auch nach 30 Jahren. Zeit nur zu
zweit, ohne Kinder, ohne Handy.</li>
<li><b>Kleine Aufmerksamkeiten:</b> Der Lieblingstee, eine Nachricht
zwischendurch, ein Kompliment.</li>
<li><b>Gemeinsame Projekte:</b> Etwas, das man zusammen aufbaut &ndash; ein
Garten, eine Reise, ein Hobby.</li>
</ul>

""" + tip("Führt eine &bdquo;Wir-Zeit&ldquo; ein, die heilig ist. Egal wie "
          "voll der Kalender: Dieser eine Abend in der Woche gehört nur euch. "
          "Behandelt ihn wie einen wichtigen Termin, den man nicht absagt.") + """

<h2>Sich gemeinsam weiterentwickeln</h2>
<p>Menschen verändern sich über die Jahre &ndash; das ist gut. Die Gefahr:
sich auseinander statt aufeinander zu zu entwickeln. Bleibt neugierig
aufeinander. Der Mensch neben dir mit 50 ist nicht mehr derselbe wie mit 25.
Lerne ihn immer wieder neu kennen, statt von einem alten Bild auszugehen.</p>

""" + box("<b>Die wichtigste Frage für Langzeitpaare:</b> &bdquo;Wie geht es "
          "dir &ndash; wirklich?&ldquo; Und dann zuhören, ohne gleich Lösungen "
          "zu bieten. Stell sie regelmäßig.") + """

<h2>Die Ehe nach den Kindern</h2>
<p>Wenn die Kinder ausziehen (das &bdquo;leere Nest&ldquo;), stehen viele
Paare plötzlich vor einem Fremden &ndash; sie haben jahrelang nur noch als
Eltern funktioniert, nicht als Paar. Das ist eine kritische, aber auch
wunderbare Phase: Ihr dürft euch wieder als Liebende neu entdecken.</p>

""" + tip("Pflegt schon WÄHREND der Elternzeit die Paarbeziehung, nicht nur "
          "die Elternrolle. Die beste Vorsorge für das leere Nest ist, nie ganz "
          "aufgehört zu haben, ein Paar zu sein.") + """

<h2>Dankbarkeit als Lebenshaltung</h2>
<p>Langzeitpaare, die glücklich sind, haben eines gemeinsam: Sie schauen mehr
auf das, was da ist, als auf das, was fehlt. Sie nehmen das Gute nicht als
selbstverständlich. Dankbarkeit, regelmäßig ausgesprochen, ist vielleicht das
stärkste Beziehungsgeheimnis überhaupt.</p>
""")

# ---------------------------------------------------------------------------
add("Wenn es kriselt", """
<h1>Kapitel 12 &ndash; Wenn es kriselt</h1>
<p class="lead">Jede Beziehung gerät irgendwann in eine Krise. Die Frage ist
nicht ob, sondern wie ihr damit umgeht.</p>

<h2>Routine und Langeweile</h2>
<p>Wenn alles immer gleich läuft, schläft das Lebendige ein. Das Gegenmittel
ist nicht der dramatische Neuanfang, sondern das bewusste Durchbrechen von
Mustern: neue Orte, neue gemeinsame Erlebnisse, kleine Überraschungen. Das
Gehirn verbindet Aufregung und Neues mit Anziehung &ndash; nutzt das.</p>

""" + tip("Macht zusammen etwas, das ihr beide noch nie gemacht habt &ndash; "
          "ein Tanzkurs, eine Klettertour, eine Reise an einen unbekannten Ort. "
          "Gemeinsam Neues zu erleben, weckt das alte Knistern überraschend "
          "zuverlässig.") + """

<h2>Emotionale Distanz</h2>
<p>Oft entsteht Distanz schleichend &ndash; durch Kränkungen, die nie
ausgesprochen wurden, durch Stress, durch Gewöhnung. Plötzlich lebt man
nebeneinander her. Hier hilft nur, die Distanz zu benennen, statt sie zu
ignorieren: &bdquo;Ich vermisse uns. Ich möchte wieder näher zu dir.&ldquo;</p>

""" + bsp("Eine Frau hatte über Jahre hunderte kleine Enttäuschungen "
          "geschluckt, um &bdquo;keinen Streit zu machen&ldquo;. Irgendwann war "
          "sie innerlich gegangen, lange bevor sie äußerlich ging. Hätte sie die "
          "kleinen Dinge früher angesprochen, wäre es nie so weit gekommen. "
          "Schweigen schützt die Liebe nicht &ndash; es höhlt sie aus.") + """

<h2>Lebenskrisen, die das Paar treffen</h2>
<p>Krankheit, Jobverlust, der Tod eines Kindes oder Elternteils, finanzielle
Not &ndash; solche Schicksalsschläge erschüttern jede Beziehung. Wichtig zu
wissen: Menschen trauern und bewältigen Krisen unterschiedlich. Der eine will
reden, der andere sich vergraben. Das ist kein Liebesentzug, sondern ein
anderer Bewältigungsstil. Versteht das, statt es persönlich zu nehmen.</p>

""" + box("<b>In schweren Krisen gilt:</b> Ihr müsst nicht stark sein "
          "füreinander &ndash; ihr dürft gemeinsam schwach sein. Das verbindet "
          "oft tiefer als jede schöne Zeit. Und scheut euch nicht, professionelle "
          "Hilfe zu holen. Das ist keine Schwäche, sondern Verantwortung.") + """

<h2>Wann ist eine Krise noch zu retten?</h2>
<p>Fast immer &ndash; solange beide noch wollen und solange es noch Respekt
gibt. Verloren ist eine Beziehung meist erst, wenn an die Stelle von Wut
Gleichgültigkeit getreten ist. Wut zeigt: Da ist noch etwas, das wehtut, weil
es wichtig ist. Gleichgültigkeit ist das eigentliche Ende.</p>

""" + tip("Wenn ihr aus eigener Kraft nicht mehr weiterkommt: Geht zu einer "
          "Paarberatung &ndash; und zwar früh, nicht erst, wenn alles in "
          "Trümmern liegt. Die meisten Paare kommen Jahre zu spät. Eine "
          "Beratung ist wie ein Personal Trainer für eure Beziehung, keine "
          "Bankrotterklärung.") + """
""")

# ---------------------------------------------------------------------------
add("Familie, Kinder und Patchwork", """
<h1>Kapitel 13 &ndash; Familie, Kinder und Patchwork</h1>
<p class="lead">Kinder sind ein Geschenk &ndash; und eine der größten
Belastungsproben für jede Paarbeziehung.</p>

<h2>Vom Paar zu Eltern</h2>
<p>Mit dem ersten Kind verändert sich alles: Schlafmangel, neue Rollen, weniger
Zeit für Zweisamkeit. Studien zeigen, dass die Beziehungszufriedenheit nach
der Geburt oft sinkt &ndash; nicht weil die Liebe schwindet, sondern weil das
Paar sich selbst vergisst über der Elternrolle.</p>

""" + tip("Bleibt auch als frischgebackene Eltern ein PAAR, nicht nur Mutter "
          "und Vater. Organisiert euch bewusst Inseln der Zweisamkeit &ndash; "
          "und sei es nur eine halbe Stunde, wenn das Kind schläft, in der ihr "
          "NICHT über das Kind redet.") + """

<h2>Erziehung als Team</h2>
<p>Kinder spüren sofort, wenn die Eltern nicht an einem Strang ziehen &ndash;
und spielen sie gegeneinander aus. Klärt Erziehungsfragen unter euch, nicht
vor dem Kind. Tretet nach außen als Einheit auf, auch wenn ihr intern
unterschiedlicher Meinung seid.</p>

""" + bsp("Ein Paar stritt ständig vor den Kindern über Erziehung &ndash; sie "
          "streng, er nachgiebig. Die Kinder lernten schnell, beim Papa zu "
          "fragen, wenn die Mama Nein gesagt hatte. Erst als die Eltern ihre "
          "Linie unter sich abstimmten und gemeinsam vertraten, kehrte Ruhe ein "
          "&ndash; und das Paar hörte auf, sich über die Kinder zu zerstreiten.") + """

<h2>Patchwork &ndash; die hohe Schule</h2>
<p>Eine neue Liebe mit Kindern aus früheren Beziehungen zusammenzuführen, ist
anspruchsvoll. Hier ein paar erprobte Wahrheiten:</p>
<ul>
<li><b>Geduld:</b> Eine Patchwork-Familie wächst über Jahre zusammen, nicht
über Nacht. Erwarte keine sofortige &bdquo;große glückliche Familie&ldquo;.</li>
<li><b>Keine Konkurrenz zum leiblichen Elternteil:</b> Du ersetzt niemanden.
Du bist eine zusätzliche erwachsene Bezugsperson &ndash; das ist genug und
wertvoll.</li>
<li><b>Erziehung der Stiefkinder:</b> Am Anfang sollte der leibliche
Elternteil die Hauptverantwortung für Regeln und Konsequenzen tragen. Der
neue Partner baut erst eine Beziehung auf, bevor er erzieht.</li>
<li><b>Das Paar zuerst:</b> Eine starke Paarbeziehung ist das Fundament, auf
dem Patchwork überhaupt erst gelingen kann.</li>
</ul>

""" + box("<b>Häufige Falle:</b> Loyalitätskonflikte. Das Kind hat Angst, den "
          "abwesenden Elternteil zu &bdquo;verraten&ldquo;, wenn es den neuen "
          "Partner mag. Nimm das ernst, mach keinen Druck, sprich nie schlecht "
          "über den anderen Elternteil. Gib dem Kind die Erlaubnis, alle lieb "
          "zu haben.") + """

<h2>Wenn das Paar ohne Kinder bleibt</h2>
<p>Nicht jedes Paar hat oder will Kinder &ndash; aus Entscheidung oder weil
es nicht klappt. Ungewollte Kinderlosigkeit ist ein tiefer Schmerz, der
Paare auf die Probe stellt. Wichtig: Macht einander keine Vorwürfe, trauert
gemeinsam, und findet zusammen einen neuen Sinn. Eine Beziehung kann auch
ohne Kinder erfüllt und vollständig sein.</p>
""")

# ---------------------------------------------------------------------------
add("Geld, Alltag und das echte Leben", """
<h1>Kapitel 14 &ndash; Geld, Alltag und das echte Leben</h1>
<p class="lead">Liebe lebt nicht nur von Romantik. Sie lebt auch von der
Frage, wer den Müll rausbringt &ndash; und wem das Geld gehört.</p>

<h2>Geld &ndash; das letzte Tabu</h2>
<p>Über Sex reden Paare heute leichter als über Geld. Dabei ist Geld einer
der häufigsten Streitpunkte überhaupt &ndash; und selten geht es nur um Zahlen.
Geld steht für Sicherheit, Macht, Freiheit, Anerkennung. Wenn ihr über Geld
streitet, geht es oft um etwas Tieferes.</p>

""" + bsp("Sie wollte sparen, er wollte das Leben genießen. Jahrelang "
          "bekriegten sie sich. In Wahrheit hatte sie als Kind Armut erlebt und "
          "Geld bedeutete für sie Sicherheit; er hatte einen früh verstorbenen "
          "Vater und Geld bedeutete für ihn, das Leben nicht zu verpassen. Beide "
          "hatten gute Gründe. Erst das Verständnis dieser Hintergründe brachte "
          "Frieden &ndash; und einen Kompromiss aus Sparen UND Genießen.") + """

""" + tip("Sprecht offen über eure Einstellung zu Geld &ndash; und über eure "
          "Geld-Geschichte aus der Kindheit. Ein bewährtes Modell für Paare: "
          "drei Konten &ndash; deins, meins, unseres. Gemeinsame Kosten laufen "
          "übers Gemeinschaftskonto, jeder behält etwas Eigenes für die "
          "persönliche Freiheit.") + """

<h2>Die unsichtbare Last: Mental Load</h2>
<p>Es reicht nicht, Aufgaben zu erledigen &ndash; jemand muss auch an sie
denken, sie planen, im Kopf behalten. Diese unsichtbare Organisationsarbeit
(&bdquo;Mental Load&ldquo;) lastet oft einseitig auf einer Person und führt zu
Erschöpfung und Groll, auch wenn der andere &bdquo;doch hilft&ldquo;.</p>

""" + box("<b>Wichtig:</b> &bdquo;Helfen&ldquo; ist das falsche Wort. Wer "
          "&bdquo;hilft&ldquo;, sieht die Aufgabe als die des anderen an. "
          "Übernehmt stattdessen ganze Bereiche eigenverantwortlich &ndash; mit "
          "Denken, Planen und Erledigen. Nicht &bdquo;Sag mir, was ich tun "
          "soll&ldquo;, sondern &bdquo;Der Bereich gehört mir.&ldquo;") + """

<h2>Faire Aufteilung</h2>
<p>Faire Aufteilung heißt nicht zwingend 50/50 bei jeder einzelnen Aufgabe,
sondern ein Gefühl von Ausgewogenheit über das Ganze &ndash; auch unter
Berücksichtigung von Erwerbsarbeit, Care-Arbeit und Belastung. Setzt euch
hin und macht es sichtbar: Wer macht eigentlich was? Oft erschrecken Paare,
wie schief die Verteilung wirklich ist.</p>

""" + tip("Macht eine Liste ALLER anfallenden Aufgaben &ndash; auch der "
          "unsichtbaren (Geschenke besorgen, Arzttermine, Vorräte im Blick "
          "haben). Verteilt sie bewusst neu. Überprüft die Aufteilung alle paar "
          "Monate, denn das Leben ändert sich.") + """

<h2>Freiraum und Gemeinsamkeit</h2>
<p>Ein gesundes Paar atmet &ndash; mal nah, mal mit Abstand. Jeder braucht
eigene Freunde, eigene Hobbys, Zeit für sich. Wer komplett verschmilzt,
verliert sich selbst &ndash; und auf Dauer auch die Anziehung. Gönnt einander
die Freiheit, auch mal ohne den anderen glücklich zu sein.</p>
""")

# ---------------------------------------------------------------------------
add("Trennung, Loslassen und Neuanfang", """
<h1>Kapitel 15 &ndash; Trennung, Loslassen und Neuanfang</h1>
<p class="lead">Manchmal ist die liebevollste Entscheidung, loszulassen. Eine
Trennung ist kein Scheitern &ndash; manchmal ist sie Mut.</p>

<h2>Wann ist es Zeit zu gehen?</h2>
<p>Es gibt keine allgemeingültige Antwort, aber einige klare Zeichen:</p>
<ul>
<li>Wenn Gewalt im Spiel ist &ndash; körperlich oder seelisch. Dann gilt:
sofort Schutz suchen. (Hilfetelefon Gewalt gegen Frauen in Deutschland:
08000 116 016, rund um die Uhr, kostenlos. Hilfetelefon Gewalt an Männern:
0800 123 9900.)</li>
<li>Wenn nur noch einer kämpft und der andere längst aufgegeben hat.</li>
<li>Wenn grundlegende Werte oder Lebensziele unvereinbar sind (z.&nbsp;B.
Kinderwunsch).</li>
<li>Wenn aus Liebe dauerhafte Gleichgültigkeit oder Verachtung geworden
ist und alle Versuche gescheitert sind.</li>
</ul>

""" + box("<b>Aber Vorsicht:</b> Verwechsle eine normale Krise nicht mit dem "
          "Ende. Viele trennen sich in einer Phase, die mit etwas Hilfe heilbar "
          "gewesen wäre. Wenn du unsicher bist, hol dir Rat, bevor du eine "
          "endgültige Entscheidung triffst.") + """

<h2>Sich fair trennen</h2>
<p>Wenn die Entscheidung gefallen ist, trennt euch mit Würde &ndash;
besonders, wenn Kinder da sind. Kein Rosenkrieg. Der Mensch, den du einmal
geliebt hast, verdient Respekt, auch im Abschied. Sprecht es persönlich aus,
nicht per Nachricht. Erklärt, ohne zu verletzen.</p>

""" + tip("Wenn Kinder betroffen sind: Sagt es ihnen gemeinsam, betont, dass "
          "es nicht ihre Schuld ist und dass beide Eltern sie weiter lieben. "
          "Sprecht NIE schlecht über den anderen Elternteil vor den Kindern "
          "&ndash; ihr trennt euch als Paar, nicht als Eltern.") + """

<h2>Den Schmerz durchleben</h2>
<p>Eine Trennung ist ein Verlust und braucht Trauer &ndash; wie jeder Verlust.
Es gibt Phasen: Schock, Schmerz, Wut, Traurigkeit, langsam Akzeptanz. Versuche
nicht, das abzukürzen oder zu betäuben (mit Alkohol, sofortigen neuen Affären,
Arbeit ohne Ende). Erlaube dir, traurig zu sein. Es geht vorbei &ndash; das
verspreche ich dir.</p>

""" + bsp("Ein Mann stürzte sich nach der Trennung sofort in eine neue "
          "Beziehung, um den Schmerz nicht zu spüren. Sie hielt ein halbes Jahr "
          "&ndash; dann brach alles auf einmal über ihn herein. Erst als er sich "
          "erlaubte, die alte Beziehung wirklich zu betrauern, wurde er frei für "
          "etwas Neues.") + """

<h2>Aus der Beziehung lernen</h2>
<p>Jede Beziehung, auch eine gescheiterte, ist ein Lehrer. Frag dich
&ndash; ohne dich zu zerfleischen &ndash;: Was war mein Anteil? Welche Muster
will ich nicht wiederholen? Was habe ich über mich gelernt? Wer das tut,
wiederholt nicht in der nächsten Beziehung dieselbe Geschichte.</p>

""" + tip("Warte mit der nächsten festen Beziehung, bis du über die alte "
          "wirklich hinweg bist &ndash; nicht aus Regel, sondern aus Fairness "
          "dir und dem nächsten Menschen gegenüber. Du sollst ihn um seiner "
          "selbst willen wählen, nicht als Pflaster.") + """

<h2>Der Neuanfang</h2>
<p>Irgendwann kommt der Tag, an dem du wieder lachst, ohne nachzudenken, und
nach vorne schaust. Das Herz ist erstaunlich heilungsfähig. Eine Trennung ist
nicht das Ende deiner Liebesfähigkeit &ndash; oft ist sie der Anfang einer
klügeren, bewussteren Liebe.</p>
""")

# ---------------------------------------------------------------------------
add("Selbstliebe", """
<h1>Kapitel 16 &ndash; Selbstliebe: das Fundament von allem</h1>
<p class="lead">Du kannst einen anderen Menschen nur so gut lieben, wie du
gelernt hast, dich selbst zu lieben.</p>

<h2>Warum Selbstliebe keine Eitelkeit ist</h2>
<p>Selbstliebe wird oft missverstanden als Egoismus oder Selbstverliebtheit.
In Wahrheit ist sie das Gegenteil: Sie ist die Fähigkeit, sich selbst mit
derselben Freundlichkeit zu behandeln, die man einem guten Freund
entgegenbringt. Wer sich selbst ständig abwertet, kann die Liebe eines
anderen gar nicht annehmen &ndash; weil er sie innerlich für unverdient hält.</p>

""" + bsp("Eine Frau konnte kein Kompliment annehmen. Sagte ihr Mann &bdquo;Du "
          "siehst schön aus&ldquo;, antwortete sie &bdquo;Ach, ich seh furchtbar "
          "aus.&ldquo; Mit der Zeit hörte er auf, Komplimente zu machen &ndash; "
          "wozu auch? Sie fühlte sich daraufhin ungeliebt. In Wahrheit hatte ihre "
          "fehlende Selbstliebe die Zuneigung abgewehrt, die da war.") + """

<h2>Der innere Kritiker</h2>
<p>In den meisten von uns wohnt eine harte Stimme, die uns kleinmacht:
&bdquo;Du bist nicht gut genug, nicht schön genug, nicht liebenswert.&ldquo;
Diese Stimme ist nicht die Wahrheit &ndash; sie ist meist die übernommene
Stimme alter Verletzungen. Du kannst lernen, ihr eine freundlichere Stimme
entgegenzusetzen.</p>

""" + tip("Wenn dein innerer Kritiker zuschlägt, frag dich: &bdquo;Würde ich "
          "so mit meinem besten Freund reden?&ldquo; Wenn nicht &ndash; warum "
          "dann mit dir selbst? Sprich mit dir, wie du mit einem geliebten "
          "Menschen sprechen würdest.") + """

<h2>Eigene Bedürfnisse ernst nehmen</h2>
<p>Wer sich selbst liebt, kennt seine Bedürfnisse und steht für sie ein
&ndash; ohne Schuldgefühle. Er kann &bdquo;Nein&ldquo; sagen, ohne sich zu
rechtfertigen, und &bdquo;Ja&ldquo; zu dem, was ihm guttut. In einer
Beziehung ist das entscheidend: Wer sich ständig aufopfert und die eigenen
Bedürfnisse verleugnet, wird auf Dauer verbittern.</p>

""" + box("<b>Wichtig:</b> Erwarte nicht, dass dein Partner dein Selbstwert-"
          "gefühl repariert. Das kann kein Mensch leisten &ndash; und es ist "
          "eine erdrückende Last für jede Beziehung. Dein Partner kann dich "
          "lieben und bestärken, aber den Frieden mit dir selbst musst du selbst "
          "schließen.") + """

<h2>Selbstliebe ist erlernbar</h2>
<p>Niemand wird mit perfektem Selbstwert geboren, und niemand ist dazu
verdammt, ihn nie zu finden. Es ist eine Übung &ndash; ein Leben lang. Kleine
Schritte: gut für den eigenen Körper sorgen, sich Fehler verzeihen, sich für
Erreichtes loben, Grenzen setzen, sich mit Menschen umgeben, die einem
guttun.</p>

""" + tip("Beginne und beende den Tag mit einem freundlichen Gedanken über "
          "dich selbst. Klingt kitschig, wirkt aber. Was wir uns täglich sagen, "
          "formt mit der Zeit, wie wir uns fühlen.") + """

<p class="center"><i>Du bist liebenswert &ndash; nicht weil dich jemand liebt,
sondern einfach, weil du bist. Fang bei dir selbst an.</i></p>
""")

# ---------------------------------------------------------------------------
add("50 Tipps zum Schluss", """
<h1>Schlusswort &ndash; 50 Tipps für die Liebe</h1>
<p class="lead">Zum Abschied das Wichtigste aus diesem Buch in 50 kurzen
Sätzen &ndash; zum Wiederlesen, wann immer du sie brauchst.</p>

<ol>
<li>Verliebtheit vergeht &ndash; Liebe ist eine tägliche Entscheidung.</li>
<li>Sprich in Ich-Botschaften, nicht in Vorwürfen.</li>
<li>Höre zu, um zu verstehen, nicht um zu antworten.</li>
<li>Wiederhole, was dein Partner gesagt hat, bevor du reagierst.</li>
<li>Streite um Lösungen, nicht um den Sieg.</li>
<li>Geh nie wütend ins Bett, ohne wenigstens Frieden zu schließen.</li>
<li>Sag täglich mindestens einmal &bdquo;danke&ldquo;.</li>
<li>Mach Komplimente &ndash; und mein sie ehrlich.</li>
<li>Berührt euch jeden Tag liebevoll.</li>
<li>Lacht zusammen, so oft es geht.</li>
<li>Pflegt einen festen Date-Abend &ndash; auch nach Jahrzehnten.</li>
<li>Verabschiedet und begrüßt euch bewusst, nie im Vorbeigehen.</li>
<li>Frage regelmäßig: &bdquo;Wie geht es dir &ndash; wirklich?&ldquo;</li>
<li>Kenne deine Liebessprache &ndash; und die deines Partners.</li>
<li>Gib Liebe in der Sprache des anderen, nicht in deiner.</li>
<li>Vermeide die vier Gifte: Kritik, Verachtung, Abwehr, Mauern.</li>
<li>Eine echte Entschuldigung enthält kein &bdquo;aber&ldquo;.</li>
<li>Verzeihe &ndash; nicht für den anderen, für deinen eigenen Frieden.</li>
<li>Sprich Kleinigkeiten an, bevor sie zu großen Bomben werden.</li>
<li>Schweigen schützt die Liebe nicht &ndash; es höhlt sie aus.</li>
<li>Triff schwierige Gespräche nicht, wenn ihr müde, hungrig oder wütend seid.</li>
<li>Nimm eine Pause, wenn der Streit eskaliert &ndash; aber kehre zurück.</li>
<li>Grab keine alten Sünden aus. Bleib beim aktuellen Thema.</li>
<li>&bdquo;Immer&ldquo; und &bdquo;nie&ldquo; haben im Streit nichts verloren.</li>
<li>Vertrauen wächst aus tausend kleinen verlässlichen Momenten.</li>
<li>Eifersucht ist meist deine Angst, nicht sein Vergehen.</li>
<li>Kontrolle ist keine Liebe &ndash; sie erstickt sie.</li>
<li>Rede über Sex &ndash; liebevoll, konkret, außerhalb des Schlafzimmers.</li>
<li>Unterschiedliche Lust ist normal, kein Defekt.</li>
<li>Nähe muss nicht immer in Sex münden.</li>
<li>Bleibt neugierig aufeinander &ndash; Menschen verändern sich.</li>
<li>Gönnt einander Freiraum &ndash; jeder braucht ein eigenes Leben.</li>
<li>Sprecht offen über Geld und eure Geld-Geschichte.</li>
<li>Teilt die unsichtbare Last (Mental Load) fair.</li>
<li>&bdquo;Helfen&ldquo; reicht nicht &ndash; übernehmt ganze Bereiche.</li>
<li>Bleibt ein Paar, auch wenn ihr Eltern werdet.</li>
<li>Zieht in der Erziehung an einem Strang &ndash; nicht vor den Kindern streiten.</li>
<li>Patchwork braucht Geduld &ndash; Jahre, nicht Wochen.</li>
<li>Sprich nie schlecht über den anderen Elternteil vor den Kindern.</li>
<li>Liebe ist Liebe &ndash; egal wen du liebst.</li>
<li>Eure Beziehung soll ein sicherer Hafen sein, gerade gegen Ablehnung von außen.</li>
<li>Hol dir früh Hilfe &ndash; Beratung ist Stärke, nicht Versagen.</li>
<li>Gleichgültigkeit ist gefährlicher als Wut.</li>
<li>Trennung ist kein Scheitern &ndash; manchmal ist sie Mut.</li>
<li>Bei Gewalt gilt nur eins: Schutz suchen, sofort.</li>
<li>Durchlebe Trennungsschmerz, statt ihn zu betäuben.</li>
<li>Lerne aus jeder Beziehung &ndash; auch aus den gescheiterten.</li>
<li>Du bist ein ganzer Mensch, kein halber auf Partnersuche.</li>
<li>Du kannst nur so gut lieben, wie du dich selbst liebst.</li>
<li>Liebe ist kein Zufall, der dir passiert &ndash; sie ist eine Kunst, die du lernst.</li>
</ol>

<hr/>
<p class="center"><b>Danke, dass du dieses Buch gelesen hast.</b></p>
<p class="center"><i>Möge deine Liebe &ndash; zu anderen und zu dir selbst &ndash;
wachsen und dich tragen, ein Leben lang.</i></p>
<p class="center">&#10084;</p>

<hr/>
<p style="font-size:0.85em;color:#777;"><b>Hinweis:</b> Dieses E-Book ersetzt
keine Therapie oder ärztliche Behandlung. Bei anhaltendem seelischem Leid,
Gewalt oder akuten Krisen wende dich bitte an professionelle Hilfe &ndash;
eine Paar- oder Einzelberatung, deinen Arzt oder eine Beratungsstelle. Du bist
es wert, dass dir geholfen wird.</p>
""")
