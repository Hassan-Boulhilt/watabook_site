# Italian (it). Legal pages are translations of the English originals; see the
# translation note at the end of privacy/terms.
L = dict(
    code="it",
    htmllang="it",
    dir="ltr",
    nav=dict(
        main_aria="Navigazione principale",
        home_aria="Home di Watabook",
        features="Funzioni",
        pricing="Prezzi",
        privacy="Privacy",
        terms="Termini",
        support="Assistenza",
        download="Scarica",
        menu_aria="Apri o chiudi il menu",
        language="Lingua",
        back="Torna a Watabook",
    ),
    index=dict(
        title="Watabook — Libretto di manutenzione e codici guasto",
        description="Watabook è il libretto di manutenzione che ti dice anche cosa non va. Digita o fotografa un codice guasto e ricevi una spiegazione in parole semplici, più promemoria di manutenzione, controllo di carburante e spese e un archivio documenti. Offline, senza account, senza pubblicità.",
        keywords="spie auto, significato spie cruscotto, codice guasto, promemoria cambio olio, libretto manutenzione auto, registro manutenzione, spese auto",
        og_title="Watabook — Libretto di manutenzione e codici guasto",
        og_desc="Il libretto di manutenzione che ti dice anche cosa non va, in parole semplici. Nessun dispositivo OBD, nessun account, funziona del tutto offline.",
        tw_desc="Il libretto di manutenzione che ti dice anche cosa non va, in parole semplici. Offline, senza account, senza pubblicità.",
        ld_desc="Libretto di manutenzione dell'auto con dizionario offline dei codici guasto OBD-II, riferimento delle spie del cruscotto, promemoria di manutenzione e controllo dei costi.",
        kicker="Libretto di manutenzione e codici guasto",
        h1="Il libretto di manutenzione che ti dice anche cosa non va.",
        lead="Nessun dispositivo OBD. Nessun account. Funziona del tutto offline. Nessuna pubblicità, mai. Digita o fotografa un codice guasto e Watabook lo spiega in parole semplici, più un libretto di manutenzione completo, promemoria e il significato di 36 spie del cruscotto.",
        dl_on="Scarica da",
        get_on="Disponibile su",
        free_note="<b>Gratis</b>: un veicolo, voci illimitate e il dizionario completo dei codici guasto offline. <b>Pro</b> aggiunge il resto, con 7 giorni di prova.",
        phone=dict(
            title="Rilevata mancata accensione nel cilindro 1",
            body="È stata rilevata una mancata accensione nel cilindro 1. Cause comuni: una candela usurata, una bobina di accensione difettosa o una perdita di depressione.",
            safe="Sicuro",
            gentle="In officina",
            stop="Fermati",
            row1="Cambio olio — Clio",
            row1_sub="tra 900 km",
            row2="Revisione",
            row2_sub="entro il 12 mar 2027",
        ),
        sec_features="Cosa fa Watabook",
        sec_pricing="Gratis vs. Pro",
        feats=[
            ("Capire una spia", "36 simboli del cruscotto spiegati: rossi, ambra, verdi e blu, con cosa significano e cosa fare. Digita o fotografa un codice guasto OBD-II e ricevi una spiegazione in parole semplici, un verdetto &laquo;posso continuare a guidare?&raquo;, cause probabili e una fascia di costo indicativa. Il dizionario offline e tutti i simboli funzionano senza rete."),
            ("Non saltare un tagliando", "Cambio olio, filtri, liquido freni, pneumatici, cinghia di distribuzione, rinnovo dell'assicurazione, revisione: promemoria per data, per chilometri o al primo dei due. I promemoria ricorrenti si riprogrammano non appena li segni come fatti."),
            ("Un libretto per auto", "Ogni intervento, rifornimento, spesa e nota, con contachilometri, costo e foto. Consumo e costo al chilometro calcolati per te, così sai sempre quanto costa davvero la tua auto, quest'anno e nel tempo."),
            ("Tenere i documenti", "Libretto, assicurazione e fatture, cifrati sul tuo telefono. Esporta tutto in CSV in qualsiasi momento: i tuoi dati non restano mai bloccati."),
        ],
        free=dict(
            name="Gratis",
            price="&euro;0",
            sub="Nessun account. Nessuna pubblicità, mai.",
            items=[
                "1 veicolo, voci illimitate",
                "Promemoria per data e chilometri",
                "Dizionario completo dei codici guasto offline",
                "Significato di 36 spie del cruscotto",
                "Esportazione CSV, in qualsiasi momento",
            ],
        ),
        pro=dict(
            badge="7 giorni di prova",
            name="Watabook Pro",
            price="1,99&nbsp;&euro;",
            per_month="/mese",
            sub="oppure 9,99&nbsp;&euro;/anno &middot; 19,99&nbsp;&euro; una tantum, per sempre",
            items=[
                "Veicoli illimitati",
                "Risposte IA &laquo;Spiega in modo semplice&raquo; e voce",
                "Promemoria ricorrenti intelligenti",
                "Archivio documenti con avvisi di scadenza",
                "PDF stampabile della manutenzione e analisi dei costi",
            ],
        ),
        price_note="Prezzi in EUR &middot; il tuo store mostra il prezzo locale &middot; disdici quando vuoi.<br>Le spiegazioni con IA sono informazioni generali, non una diagnosi: fai sempre controllare un guasto critico per la sicurezza da un professionista.",
    ),
    privacy=dict(
        title="Informativa sulla privacy — Watabook",
        description="Informativa sulla privacy di Watabook. Tutto ciò che inserisci resta sul tuo dispositivo: non c'è alcun account né server che conservi i tuoi dati.",
        h1="Informativa sulla privacy",
        updated="Ultimo aggiornamento: 12 settembre 2026",
        body="""        <p>Watabook è un libretto di manutenzione per la tua auto. È pensato per tenere i tuoi dati <strong>sul tuo dispositivo</strong>.</p>

        <h2 id="collect">Cosa raccogliamo</h2>
        <p><strong>Niente.</strong> Watabook non ha account, accesso, analisi, pubblicità né tracciamento. Non abbiamo alcun server che conservi le tue informazioni.</p>
        <p>Tutto ciò che inserisci (veicoli, voci di manutenzione e carburante, promemoria, documenti, cronologia dei codici guasto) viene salvato solo nella memoria privata dell'app sul tuo telefono. I documenti che aggiungi all'archivio sono cifrati sul dispositivo.</p>

        <h2 id="internet">Quando l'app usa internet</h2>
        <p>Watabook funziona del tutto offline. Contatta la rete solo per le seguenti funzioni, e solo quando le usi:</p>
        <ul>
          <li><strong>&laquo;Spiega in modo semplice&raquo; (IA):</strong> invia il codice guasto, la marca della tua auto, la lingua scelta e un identificativo casuale dell'app (non collegato a te) al nostro servizio di elaborazione, che chiede a Google Gemini una spiegazione in parole semplici. Il tuo nome, la tua email o la tua posizione non vengono mai inviati.</li>
          <li><strong>Decodifica del VIN:</strong> invia il VIN di 17 caratteri che digiti al database pubblico dei veicoli della NHTSA degli Stati Uniti, per compilare marca, modello e anno.</li>
          <li><strong>Acquisti:</strong> abbonamento e ripristino sono gestiti dalla fatturazione di Apple / Google e da RevenueCat, che riceve una ricevuta d'acquisto e un proprio identificativo anonimo, non la tua identità.</li>
          <li><strong>Esporta e condividi:</strong> quando esporti un CSV o un PDF, o condividi un documento, il menu di condivisione del tuo dispositivo lo invia dove scegli <em>tu</em>. Watabook non lo trasmette.</li>
        </ul>
        <p>Tutte queste connessioni usano HTTPS.</p>

        <h2 id="control">Il tuo controllo</h2>
        <ul>
          <li>Elimina qualsiasi voce, documento o veicolo nell'app in qualsiasi momento.</li>
          <li>Disinstallare Watabook rimuove definitivamente tutti i suoi dati dal tuo dispositivo.</li>
          <li>Non ci sono dati sul server da eliminare, perché non ne conserviamo.</li>
          <li>Esporta tutto in CSV quando vuoi: i tuoi dati non restano mai bloccati.</li>
        </ul>

        <h2 id="children">Minori</h2>
        <p>Watabook non è rivolto ai minori e non raccoglie dati da nessuno.</p>

        <h2 id="changes">Modifiche</h2>
        <p>Se questa informativa cambia, la data di &laquo;ultimo aggiornamento&raquo; qui sopra cambierà e la nuova versione sarà pubblicata qui.</p>

        <h2 id="contact">Contatti</h2>
        <div class="contact-card">
          <div class="label">Richieste sulla privacy</div>
          <p>Email: <a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a></p>
        </div>

        <p><em>Questa è una traduzione dell'originale in inglese. In caso di discrepanza prevale la versione inglese.</em></p>""",
    ),
    terms=dict(
        title="Termini di servizio — Watabook",
        description="Termini di servizio dell'app Watabook: abbonamenti, uso consentito, spiegazioni con IA e avviso di sicurezza.",
        h1="Termini di servizio",
        effective="In vigore dal: 12 settembre 2026",
        updated="Ultimo aggiornamento: 12 settembre 2026",
        body="""        <div class="note-box">
          <p>Leggi con attenzione questi Termini prima di usare Watabook. Scaricando, installando o usando l'app accetti di essere vincolato da questi Termini. Se non sei d'accordo, non usare Watabook.</p>
        </div>

        <div class="toc">
          <h3>Indice</h3>
          <ol>
            <li><a href="#acceptance">Accettazione dei Termini</a></li>
            <li><a href="#description">Descrizione del servizio</a></li>
            <li><a href="#your-data">Nessun account, i tuoi dati</a></li>
            <li><a href="#subscriptions">Abbonamenti e acquisti in-app</a></li>
            <li><a href="#acceptable-use">Uso consentito</a></li>
            <li><a href="#disclaimer">Non è una diagnosi: avviso di sicurezza</a></li>
            <li><a href="#third-party">Servizi di terze parti</a></li>
            <li><a href="#ip">Proprietà intellettuale</a></li>
            <li><a href="#warranties">Esclusione di garanzie</a></li>
            <li><a href="#liability">Limitazione di responsabilità</a></li>
            <li><a href="#termination">Cessazione</a></li>
            <li><a href="#governing">Legge applicabile</a></li>
            <li><a href="#changes-terms">Modifiche a questi Termini</a></li>
            <li><a href="#contact-terms">Contatti</a></li>
          </ol>
        </div>

        <h2 id="acceptance">1. Accettazione dei Termini</h2>
        <p>Questi Termini di servizio (&laquo;Termini&raquo;) sono un accordo giuridicamente vincolante tra te (&laquo;tu&raquo;, &laquo;Utente&raquo;) e DevAndRepair (&laquo;noi&raquo;), lo sviluppatore di Watabook, che regola il tuo accesso e utilizzo dell'applicazione mobile Watabook (l'&laquo;App&raquo;). Installando o usando l'App confermi di avere l'età sufficiente per accettare questi Termini nel tuo paese di residenza e di aver letto, compreso e accettato questi Termini e la nostra <a href="/it/privacy.html">Informativa sulla privacy</a>.</p>

        <h2 id="description">2. Descrizione del servizio</h2>
        <p>Watabook è un libretto di manutenzione per la tua auto. Conserva i tuoi veicoli, le voci di manutenzione e carburante, i promemoria e i documenti localmente sul tuo dispositivo e offre un dizionario di consultazione offline dei codici guasto OBD-II e delle spie del cruscotto. Una funzione opzionale, &laquo;Spiega in modo semplice&raquo;, invia un codice guasto al nostro servizio di elaborazione con IA per ottenere una spiegazione in parole semplici (vedi §6 e §7).</p>
        <p>Watabook è uno strumento di consultazione e registrazione. Non è uno strumento diagnostico, non si collega al tuo veicolo e non sostituisce il controllo o la riparazione da parte di un meccanico qualificato.</p>

        <h2 id="your-data">3. Nessun account, i tuoi dati</h2>
        <ul>
          <li>Watabook non ha account né accesso. Non c'è nulla che possiamo autenticare, sospendere o recuperare per te.</li>
          <li>Tutto ciò che inserisci è conservato localmente sul tuo dispositivo, come descritto nella nostra <a href="/it/privacy.html">Informativa sulla privacy</a>. Non ne conserviamo alcuna copia.</li>
          <li>Sei responsabile della sicurezza del tuo dispositivo (codice di sblocco, backup): perdere o ripristinare il dispositivo senza un backup significa perdere i tuoi dati di Watabook, perché non possiamo ripristinare ciò che non abbiamo mai avuto.</li>
          <li>Puoi esportare tutto in CSV in qualsiasi momento, e disinstallare l'App elimina definitivamente i suoi dati dal tuo dispositivo.</li>
        </ul>

        <h2 id="subscriptions">4. Abbonamenti e acquisti in-app</h2>
        <p>Watabook Pro è offerto come abbonamento mensile o annuale a rinnovo automatico, oppure come acquisto una tantum a vita. Tutti i pagamenti sono elaborati dall'App Store di Apple o da Google Play, mai direttamente da noi: non vediamo né conserviamo mai i tuoi dati di pagamento.</p>
        <ul>
          <li><strong>Prova gratuita:</strong> dove offerta, un abbonamento a rinnovo automatico inizia con un periodo di prova gratuito; se non disdici prima della fine, si converte automaticamente in un abbonamento a pagamento.</li>
          <li><strong>Rinnovo automatico:</strong> gli abbonamenti mensili e annuali si rinnovano automaticamente al prezzo mostrato al momento dell'acquisto fino alla disdetta. Gestisci o disdici un abbonamento dalle impostazioni del tuo ID Apple o del tuo account Google Play, non dall'app, perché non abbiamo un pannello di fatturazione nostro.</li>
          <li><strong>A vita:</strong> un acquisto una tantum che sblocca le funzioni Pro finché l'App esiste e continua a essere supportata, legato al tuo ID Apple o account Google, non a un account Watabook (non ne esiste uno).</li>
          <li><strong>Rimborsi:</strong> gestiti interamente da Apple o Google secondo le loro politiche di rimborso. Non possiamo emettere direttamente un rimborso.</li>
          <li><strong>Ripristino degli acquisti:</strong> reinstallando l'App o passando a un nuovo dispositivo, il tuo diritto viene ripristinato automaticamente tramite il tuo ID Apple / account Google, senza bisogno di accedere.</li>
        </ul>

        <h2 id="acceptable-use">5. Uso consentito</h2>
        <p>Ti impegni a non:</p>
        <ul>
          <li>effettuare il reverse engineering, decompilare o manomettere l'App oltre quanto consentito dai termini della tua piattaforma;</li>
          <li>usare la funzione &laquo;Spiega in modo semplice&raquo; per inviare qualcosa di diverso da un vero codice guasto OBD-II e da una domanda di approfondimento in buona fede;</li>
          <li>tentare di aggirare i limiti di frequenza, i controlli sui diritti o i limiti della versione gratuita dell'App;</li>
          <li>usare l'App per scopi illeciti.</li>
        </ul>

        <h2 id="disclaimer">6. Non è una diagnosi: avviso di sicurezza</h2>
        <div class="note-box">
          <p>Ogni spiegazione di un codice guasto, sia del dizionario offline integrato sia della funzione IA &laquo;Spiega in modo semplice&raquo;, è <strong>un'informazione generale, non una diagnosi</strong>. Non ispeziona il tuo veicolo. Fai sempre controllare un guasto critico per la sicurezza da un meccanico qualificato prima di continuare a guidare.</p>
        </div>
        <p>Cause probabili, fasce di costo, idoneità al fai-da-te e indicazioni su &laquo;posso continuare a guidare?&raquo; sono stime pensate per aiutarti a compiere un passo successivo ragionevole, non un sostituto dell'ispezione professionale. Watabook e DevAndRepair non sono responsabili di alcuna decisione presa, né di danni, lesioni o perdite derivanti dall'affidamento a queste informazioni (vedi §10).</p>

        <h2 id="third-party">7. Servizi di terze parti</h2>
        <p>L'App si basa su servizi che non controlliamo, ciascuno regolato dai propri termini:</p>
        <ul>
          <li>Il dizionario dei codici guasto offline si basa sui dati del progetto open source <a href="https://github.com/Wal33D/DTC-Database" target="_blank" rel="noopener">DTC-Database</a> (licenza MIT), tradotti automaticamente nelle altre lingue dell'App.</li>
          <li>&laquo;Spiega in modo semplice&raquo; è generato da Google Gemini, chiamato tramite il nostro servizio di elaborazione: l'App non detiene mai direttamente una chiave di accesso.</li>
          <li>La decodifica del VIN usa il database vPIC, gratuito e pubblico, della NHTSA degli Stati Uniti.</li>
          <li>Gli abbonamenti sono fatturati da Apple / Google e gestiti tramite RevenueCat.</li>
        </ul>
        <p>Non siamo responsabili della disponibilità o dell'accuratezza di questi servizi di terze parti.</p>

        <h2 id="ip">8. Proprietà intellettuale</h2>
        <p>L'app Watabook, il suo design e i suoi contenuti originali sono di proprietà di DevAndRepair. Non puoi copiare, riprodurre o creare opere derivate dall'App stessa. Mantieni la piena proprietà dei dati che inserisci (dati del veicolo, note, foto, documenti); non rivendichiamo alcun diritto su di essi e, poiché non lasciano mai il tuo dispositivo, non potremmo usarli nemmeno volendo.</p>

        <h2 id="warranties">9. Esclusione di garanzie</h2>
        <p>L'App è fornita &laquo;così com'è&raquo; e &laquo;come disponibile&raquo;, senza garanzie di alcun tipo, espresse o implicite, inclusa l'idoneità a uno scopo particolare o la non violazione di diritti, nella massima misura consentita dalla legge.</p>

        <h2 id="liability">10. Limitazione di responsabilità</h2>
        <p>Nella massima misura consentita dalla legge, la responsabilità complessiva di DevAndRepair derivante dal tuo uso dell'App non supererà l'importo che ci hai pagato nei 12 mesi precedenti la richiesta, o 20&nbsp;&euro;, se maggiore. Non siamo responsabili di danni indiretti, incidentali o consequenziali, compresi quelli derivanti da una decisione di riparazione di un veicolo presa sulla base di informazioni dell'App.</p>

        <h2 id="termination">11. Cessazione</h2>
        <p>Puoi smettere di usare l'App e disinstallarla in qualsiasi momento; così facendo i suoi dati locali vengono eliminati (vedi §3). Possiamo ritirare l'App dall'App Store o da Google Play, o interrompere una funzione, a nostra discrezione; ove ragionevolmente possibile daremo avviso tramite la scheda dello store o questa pagina.</p>

        <h2 id="governing">12. Legge applicabile</h2>
        <p>Questi Termini sono regolati dalla legge della giurisdizione in cui opera DevAndRepair, senza riguardo alle norme sui conflitti di legge. Qualsiasi controversia sarà affrontata innanzitutto tramite negoziazione in buona fede; se non risolta, sarà sottoposta ai tribunali competenti di tale giurisdizione. Se una disposizione di questi Termini non fosse applicabile, le altre restano in vigore.</p>

        <h2 id="changes-terms">13. Modifiche a questi Termini</h2>
        <p>Possiamo aggiornare questi Termini di volta in volta. La data di &laquo;ultimo aggiornamento&raquo; qui sopra cambierà e la nuova versione sarà pubblicata qui. Continuare a usare l'App dopo una modifica significa accettare i Termini aggiornati.</p>

        <h2 id="contact-terms">14. Contatti</h2>
        <div class="contact-card">
          <div class="label">Richieste sui Termini</div>
          <p>Email: <a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a><br>
          Sito web: <a href="https://watabook.devandrepair.com">watabook.devandrepair.com</a></p>
        </div>

        <p><em>Questa è una traduzione dell'originale in inglese. In caso di discrepanza prevale la versione inglese.</em></p>""",
    ),
    support=dict(
        title="Assistenza — Watabook",
        description="Assistenza di Watabook: contatti e domande frequenti su uso offline, abbonamenti, i tuoi dati e spiegazioni con IA.",
        h1="Assistenza",
        reply="Di solito rispondiamo entro 2 giorni lavorativi.",
        body="""        <div class="contact-card">
          <div class="label">Contattaci</div>
          <p>Email: <a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a><br>
          Indica il tuo dispositivo (iPhone/Android), la versione dell'app e cosa è successo: uno screenshot aiuta.</p>
        </div>

        <h2 id="faq">Domande frequenti</h2>

        <h3>Serve una connessione a internet?</h3>
        <p>No. Il libretto di manutenzione, i promemoria, l'archivio documenti e l'intero dizionario offline dei codici guasto e delle spie del cruscotto funzionano senza alcun segnale. Solo &laquo;Spiega in modo semplice&raquo; (IA) e la compilazione automatica del VIN richiedono una connessione, ed entrambi continuano a funzionare in modo ordinato, senza errori, quando manca.</p>

        <h3>Ho disdetto Pro: cosa succede ai miei dati?</h3>
        <p>Niente. Il tuo libretto, i promemoria e i documenti restano esattamente come sono; l'app torna semplicemente ai limiti della versione gratuita (un veicolo, un documento salvato). Non viene eliminato nulla.</p>

        <h3>Come disdico o ripristino un abbonamento?</h3>
        <p>Gli abbonamenti sono fatturati da Apple o Google, non da noi: gestiscili, disdicili o ripristinali dal tuo ID Apple (Impostazioni &rarr; il tuo nome &rarr; Abbonamenti) o da Google Play (Play Store &rarr; Menu &rarr; Pagamenti e abbonamenti).</p>

        <h3>Posso riavere i miei dati se perdo il telefono?</h3>
        <p>Solo dal backup del tuo dispositivo (iCloud / backup Google): Watabook non ha account né copia sul server, per scelta progettuale (vedi la nostra <a href="/it/privacy.html">Informativa sulla privacy</a>). Esportare ogni tanto un backup in CSV è una buona abitudine.</p>

        <h3>La spiegazione dell'IA è una vera diagnosi?</h3>
        <p>No: è un'informazione generale per aiutarti a capire un codice guasto, mai un sostituto del controllo di un meccanico. Vedi i nostri <a href="/it/terms.html#disclaimer">Termini, §6</a>.</p>""",
    ),
)
