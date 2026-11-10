# Web sales — Terms section 4 and Privacy additions, per language.
# Applied by tools/build_locales.py to the generated languages (ar, de, es,
# pt, it) and once to the hand-written French pages. English pages were
# edited by hand with the same content.
# Keys:
#   privacy: updated, collect (replaces the first <p> of the 1st section),
#            license_li (inserted after the 3rd <li> of the 2nd section),
#            section (inserted before the 3rd <h2>), control_li (replaces the
#            3rd <li> of the 3rd section), children (replaces the <p> of the
#            4th section)
#   terms:   updated, toc4 (text of the 4th TOC entry), section4 (replaces the
#            whole 4th section, from its <h2> to the next <h2>)

MAIL = '<a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a>'

LEGAL = {}

LEGAL["fr"] = dict(
    privacy=dict(
        updated="Dernière mise à jour : 10 novembre 2026",
        collect='<p><strong>Rien depuis l’app.</strong> Watabook n’a ni compte, ni connexion, ni statistiques, ni publicité, ni pistage. Nous n’avons pas de serveur qui stocke ce que vous saisissez dans l’app.</p>\n        <p>Seule exception : l’achat de Pro sur ce site. Nous gardons alors un petit dossier de licence, décrit dans <a href="#achat-web">Si vous achetez Pro sur ce site</a> ci-dessous.</p>',
        license_li="<li><strong>Clé de licence (Android, achetée sur ce site) :</strong> quand vous saisissez une clé, l’app envoie la clé et un identifiant d’appareil aléatoire qu’elle a créé à notre service de licences, une fois pour l’activer puis environ une fois par mois pour vérifier qu’elle est toujours valide. L’app n’envoie ni nom, ni e-mail, ni position.</li>",
        section=f'''<h2 id="achat-web">Si vous achetez Pro sur ce site</h2>
        <p>Les paiements sur ce site sont traités par <strong>PayPal</strong>. Nous ne voyons ni ne stockons jamais vos données de carte ou bancaires. Pour vous fournir une clé de licence, notre service de licences conserve :</p>
        <ul>
          <li>l’adresse e-mail que PayPal nous transmet pour votre achat, afin d’envoyer votre clé et de vous aider si vous la perdez ;</li>
          <li>votre clé de licence, la formule, sa date d’expiration, et les identifiants de commande ou d’abonnement et de paiement PayPal ;</li>
          <li>pour chaque appareil où vous activez la clé : l’identifiant d’appareil aléatoire, un nom d’appareil facultatif, et les dates d’activation et de dernière vérification.</li>
        </ul>
        <p>Le service de licences fonctionne sur Cloudflare. Les e-mails de clé sont envoyés via Resend. Nous utilisons votre e-mail uniquement pour votre clé et pour vos questions sur votre achat, jamais pour du marketing sauf si vous l’acceptez séparément.</p>
        <p>Nous gardons le dossier de licence tant que votre licence est valide, puis aussi longtemps que la loi l’exige pour la comptabilité. Vous pouvez demander à le consulter ou à le supprimer à {MAIL} ; sa suppression met fin à la licence.</p>

        ''',
        control_li="<li>L’app ne garde aucune donnée sur nos serveurs. Si vous avez acheté Pro sur ce site, vous pouvez demander la suppression de votre dossier de licence (voir ci-dessus).</li>",
        children="<p>Watabook ne s’adresse pas aux enfants. L’app ne collecte aucune donnée sur personne ; les achats sur ce site sont destinés aux adultes disposant d’un compte PayPal ou d’une carte.</p>",
    ),
    terms=dict(
        updated="Dernière mise à jour : 10 novembre 2026",
        toc4="Abonnements &amp; achats",
        section4='''<h2 id="abonnements">4. Abonnements &amp; achats</h2>
        <p>Watabook Pro peut s’acheter de deux façons. Les règles dépendent de l’endroit où vous l’achetez.</p>
        <h3>Sur l’App Store ou Google Play</h3>
        <p>Les paiements sont traités par l’App Store d’Apple ou Google Play, jamais directement par nous ; nous ne voyons ni ne stockons vos données de paiement.</p>
        <ul>
          <li><strong>Essai gratuit :</strong> lorsqu’il est proposé, un abonnement à renouvellement automatique commence par une période d’essai ; sauf résiliation avant la fin, il devient payant automatiquement.</li>
          <li><strong>Renouvellement automatique :</strong> les abonnements se renouvellent au prix affiché lors de l’achat jusqu’à résiliation, depuis votre identifiant Apple ou votre compte Google Play.</li>
          <li><strong>À vie :</strong> un achat unique qui débloque Pro tant que l’App existe et reste maintenue, lié à votre identifiant Apple ou compte Google.</li>
          <li><strong>Remboursements :</strong> gérés par Apple ou Google selon leurs propres règles.</li>
          <li><strong>Restauration des achats :</strong> réinstaller l’App ou changer d’appareil restaure votre droit via votre identifiant Apple / compte Google.</li>
        </ul>
        <h3>Sur ce site (Android), avec PayPal</h3>
        <ul>
          <li><strong>Formules :</strong> Annuel, avec 7 jours d’essai gratuit puis renouvellement automatique chaque année au prix affiché, ou À vie, en un seul paiement. Les prix sont en dollars américains. Les paiements sont traités par PayPal ; nous ne voyons jamais vos données de carte ou bancaires.</li>
          <li><strong>Clé de licence :</strong> après paiement, vous recevez une clé par e-mail et sur la page. Une clé est pour votre usage personnel sur 3 appareils au maximum en même temps. Vous pouvez libérer un appareil depuis l’app ou avec un lien de réinitialisation envoyé par e-mail. Ne partagez pas et ne vendez pas votre clé ; nous pouvons bloquer les clés partagées publiquement ou utilisées contre ces Conditions.</li>
          <li><strong>Vérifications :</strong> l’App vérifie la clé en ligne une fois à l’activation puis environ une fois par mois. Sans internet, Pro continue de fonctionner pendant un délai de grâce.</li>
          <li><strong>Résiliation :</strong> résiliez l’annuel à tout moment dans votre compte PayPal. Pro reste actif jusqu’à la fin de la période payée. Résiliez pendant l’essai gratuit et rien n’est débité.</li>
          <li><strong>Remboursements :</strong> remboursement intégral sous 14 jours après tout paiement, voir la <a href="/fr/refund.html">Politique de remboursement</a>. Un paiement remboursé, annulé ou contesté désactive la clé qu’il a payée.</li>
          <li><strong>À vie :</strong> débloque Pro tant que l’App existe et reste maintenue.</li>
        </ul>

        ''',
    ),
)

LEGAL["ar"] = dict(
    privacy=dict(
        updated="آخر تحديث: 10 نوفمبر 2026",
        collect='<p><strong>لا شيء من التطبيق.</strong> لا يحتوي Watabook على حساب أو تسجيل دخول أو إحصاءات أو إعلانات أو تتبّع. لا نملك خادمًا يخزّن ما تُدخله في التطبيق.</p>\n        <p>الاستثناء الوحيد هو شراء Pro من هذا الموقع: عندها نحتفظ بسجل ترخيص صغير، موضّح في <a href="#web-purchase">إذا اشتريت Pro من هذا الموقع</a> أدناه.</p>',
        license_li="<li><strong>مفتاح الترخيص (أندرويد، المشترى من هذا الموقع):</strong> عند إدخال مفتاح، يرسل التطبيق المفتاح ومعرّف جهاز عشوائيًا أنشأه إلى خدمة التراخيص لدينا، مرة للتفعيل ثم نحو مرة كل شهر للتحقق من صلاحيته. لا يرسل التطبيق اسمًا أو بريدًا إلكترونيًا أو موقعًا.</li>",
        section=f'''<h2 id="web-purchase">إذا اشتريت Pro من هذا الموقع</h2>
        <p>تُعالَج المدفوعات على هذا الموقع عبر <strong>PayPal</strong>. لا نرى ولا نخزّن أبدًا بيانات بطاقتك أو حسابك البنكي. ولنعطيك مفتاح ترخيص، تحتفظ خدمة التراخيص لدينا بما يلي:</p>
        <ul>
          <li>البريد الإلكتروني الذي يرسله لنا PayPal لعملية الشراء، لإرسال مفتاحك ومساعدتك إن أضعته؛</li>
          <li>مفتاح الترخيص والخطة وتاريخ انتهائها، ومعرّفات طلب أو اشتراك PayPal والدفع؛</li>
          <li>لكل جهاز تفعّل عليه المفتاح: معرّف الجهاز العشوائي، واسمًا اختياريًا للجهاز، وتاريخَي التفعيل وآخر تحقق.</li>
        </ul>
        <p>تعمل خدمة التراخيص على Cloudflare، وتُرسَل رسائل المفاتيح عبر Resend. نستخدم بريدك فقط لمفتاحك ولأسئلتك عن الشراء، ولا نستخدمه للتسويق أبدًا إلا إذا وافقت على ذلك بشكل منفصل.</p>
        <p>نحتفظ بسجل الترخيص ما دام ترخيصك صالحًا، وبعد ذلك المدة التي يفرضها القانون للمحاسبة. يمكنك طلب الاطلاع عليه أو حذفه عبر {MAIL}؛ وحذفه ينهي الترخيص.</p>

        ''',
        control_li="<li>لا يحتفظ التطبيق بأي بيانات على خوادمنا. إذا اشتريت Pro من هذا الموقع، يمكنك طلب حذف سجل ترخيصك (انظر أعلاه).</li>",
        children="<p>Watabook غير موجّه للأطفال. لا يجمع التطبيق أي بيانات من أحد؛ والشراء من هذا الموقع مخصص للبالغين الذين لديهم حساب PayPal أو بطاقة.</p>",
    ),
    terms=dict(
        updated="آخر تحديث: 10 نوفمبر 2026",
        toc4="الاشتراكات والمشتريات",
        section4='''<h2 id="subscriptions">4. الاشتراكات والمشتريات</h2>
        <p>يمكن شراء Watabook Pro بطريقتين، وتختلف القواعد حسب مكان الشراء.</p>
        <h3>في App Store أو Google Play</h3>
        <p>تُعالَج المدفوعات عبر App Store من Apple أو Google Play، ولا نعالجها نحن مباشرة أبدًا؛ لا نرى ولا نخزّن بيانات الدفع الخاصة بك.</p>
        <ul>
          <li><strong>التجربة المجانية:</strong> عند توفرها، يبدأ الاشتراك المتجدد تلقائيًا بفترة تجريبية، ويتحول إلى اشتراك مدفوع تلقائيًا ما لم تلغِه قبل نهايتها.</li>
          <li><strong>التجديد التلقائي:</strong> تتجدد الاشتراكات بالسعر المعروض عند الشراء حتى تلغيها من إعدادات Apple ID أو حساب Google Play.</li>
          <li><strong>مدى الحياة:</strong> شراء لمرة واحدة يفتح Pro ما دام التطبيق موجودًا ومدعومًا، ومرتبط بـ Apple ID أو حساب Google.</li>
          <li><strong>الاسترداد:</strong> تتولاه Apple أو Google وفق سياساتهما.</li>
          <li><strong>استعادة المشتريات:</strong> إعادة تثبيت التطبيق أو تغيير الجهاز يستعيد حقك عبر Apple ID أو حساب Google.</li>
        </ul>
        <h3>على هذا الموقع (أندرويد) عبر PayPal</h3>
        <ul>
          <li><strong>الخطط:</strong> سنوية مع تجربة مجانية 7 أيام ثم تجديد تلقائي كل سنة بالسعر المعروض، أو مدى الحياة بدفعة واحدة. الأسعار بالدولار الأمريكي، وتُعالَج المدفوعات عبر PayPal؛ لا نرى أبدًا بيانات بطاقتك أو حسابك البنكي.</li>
          <li><strong>مفتاح الترخيص:</strong> بعد الدفع تتلقى مفتاحًا بالبريد الإلكتروني وفي الصفحة. المفتاح لاستخدامك الشخصي على 3 أجهزة كحد أقصى في الوقت نفسه. يمكنك تحرير جهاز من التطبيق أو برابط إعادة تعيين يُرسل إلى بريدك. لا تشارك مفتاحك ولا تبعه؛ ويحق لنا حظر المفاتيح المنشورة علنًا أو المستخدمة خلافًا لهذه الشروط.</li>
          <li><strong>التحقق:</strong> يتحقق التطبيق من المفتاح عبر الإنترنت مرة عند التفعيل ثم نحو مرة كل شهر. ودون إنترنت يظل Pro يعمل خلال مهلة سماح.</li>
          <li><strong>الإلغاء:</strong> ألغِ الخطة السنوية في أي وقت من حساب PayPal. يبقى Pro مفعّلًا حتى نهاية الفترة المدفوعة، وإذا ألغيت خلال التجربة المجانية فلن يُخصم شيء.</li>
          <li><strong>الاسترداد:</strong> استرداد كامل خلال 14 يومًا من أي دفعة، راجع <a href="/ar/refund.html">سياسة الاسترداد</a>. الدفعة المستردة أو الملغاة أو المتنازع عليها توقف المفتاح الذي دفعته.</li>
          <li><strong>مدى الحياة:</strong> يفتح ميزات Pro ما دام التطبيق موجودًا ومدعومًا.</li>
        </ul>

        ''',
    ),
)

LEGAL["de"] = dict(
    privacy=dict(
        updated="Zuletzt aktualisiert: 10. November 2026",
        collect='<p><strong>Nichts aus der App.</strong> Watabook hat kein Konto, keine Anmeldung, keine Analyse, keine Werbung und kein Tracking. Wir haben keinen Server, der speichert, was du in der App eingibst.</p>\n        <p>Die einzige Ausnahme ist der Kauf von Pro auf dieser Website: Dann speichern wir einen kleinen Lizenzdatensatz, beschrieben unter <a href="#web-purchase">Wenn du Pro auf dieser Website kaufst</a>.</p>',
        license_li="<li><strong>Lizenzschlüssel (Android, auf dieser Website gekauft):</strong> Wenn du einen Schlüssel eingibst, sendet die App den Schlüssel und eine zufällige Gerätekennung, die sie selbst erzeugt hat, an unseren Lizenzdienst – einmal zur Aktivierung und danach etwa einmal im Monat zur Prüfung. Die App sendet keinen Namen, keine E-Mail und keinen Standort.</li>",
        section=f'''<h2 id="web-purchase">Wenn du Pro auf dieser Website kaufst</h2>
        <p>Zahlungen auf dieser Website werden von <strong>PayPal</strong> abgewickelt. Wir sehen oder speichern niemals deine Karten- oder Bankdaten. Um dir einen Lizenzschlüssel zu geben, speichert unser Lizenzdienst:</p>
        <ul>
          <li>die E-Mail-Adresse, die PayPal uns für deinen Kauf übermittelt, damit wir dir deinen Schlüssel senden und helfen können, falls du ihn verlierst;</li>
          <li>deinen Lizenzschlüssel, den Tarif, sein Ablaufdatum sowie die PayPal-Bestell- oder Abonnement- und Zahlungs-IDs;</li>
          <li>für jedes Gerät, auf dem du den Schlüssel aktivierst: die zufällige Gerätekennung, einen optionalen Gerätenamen sowie das Aktivierungs- und letzte Prüfdatum.</li>
        </ul>
        <p>Der Lizenzdienst läuft bei Cloudflare. Schlüssel-E-Mails werden über Resend versendet. Wir nutzen deine E-Mail nur für deinen Schlüssel und für Fragen zu deinem Kauf, nie für Werbung, außer du stimmst dem gesondert zu.</p>
        <p>Wir speichern den Lizenzdatensatz, solange deine Lizenz gültig ist, und danach so lange, wie es das Gesetz für die Buchhaltung verlangt. Du kannst unter {MAIL} Auskunft oder Löschung verlangen; die Löschung beendet die Lizenz.</p>

        ''',
        control_li="<li>Die App speichert keine Daten auf unseren Servern. Hast du Pro auf dieser Website gekauft, kannst du die Löschung deines Lizenzdatensatzes verlangen (siehe oben).</li>",
        children="<p>Watabook richtet sich nicht an Kinder. Die App erhebt von niemandem Daten; Käufe auf dieser Website sind für Erwachsene mit PayPal-Konto oder Karte gedacht.</p>",
    ),
    terms=dict(
        updated="Zuletzt aktualisiert: 10. November 2026",
        toc4="Abonnements &amp; Käufe",
        section4='''<h2 id="subscriptions">4. Abonnements &amp; Käufe</h2>
        <p>Watabook Pro kann auf zwei Wegen gekauft werden. Die Regeln hängen davon ab, wo du kaufst.</p>
        <h3>Im App Store oder bei Google Play</h3>
        <p>Zahlungen werden vom App Store von Apple oder von Google Play abgewickelt, nie direkt von uns; wir sehen oder speichern deine Zahlungsdaten nicht.</p>
        <ul>
          <li><strong>Kostenloser Test:</strong> Wo angeboten, beginnt ein automatisch verlängertes Abonnement mit einer Testphase; wenn du nicht vorher kündigst, wird es automatisch kostenpflichtig.</li>
          <li><strong>Automatische Verlängerung:</strong> Abonnements verlängern sich zum beim Kauf angezeigten Preis, bis du über deine Apple-ID oder dein Google-Play-Konto kündigst.</li>
          <li><strong>Lebenslang:</strong> ein einmaliger Kauf, der Pro freischaltet, solange die App existiert und unterstützt wird, gebunden an deine Apple-ID oder dein Google-Konto.</li>
          <li><strong>Erstattungen:</strong> erfolgen durch Apple oder Google nach deren eigenen Richtlinien.</li>
          <li><strong>Käufe wiederherstellen:</strong> Neuinstallation oder Gerätewechsel stellt deine Berechtigung über Apple-ID / Google-Konto wieder her.</li>
        </ul>
        <h3>Auf dieser Website (Android) mit PayPal</h3>
        <ul>
          <li><strong>Tarife:</strong> Jährlich, mit 7 Tagen kostenlos und danach automatischer jährlicher Verlängerung zum angezeigten Preis, oder Lebenslang mit einer Zahlung. Preise in US-Dollar. Zahlungen wickelt PayPal ab; wir sehen niemals deine Karten- oder Bankdaten.</li>
          <li><strong>Lizenzschlüssel:</strong> Nach der Zahlung erhältst du einen Schlüssel per E-Mail und auf der Seite. Ein Schlüssel ist für deine persönliche Nutzung auf bis zu 3 Geräten gleichzeitig. Du kannst ein Gerät in der App oder per Reset-Link an deine E-Mail freigeben. Teile oder verkaufe deinen Schlüssel nicht; wir können Schlüssel sperren, die öffentlich geteilt oder entgegen diesen Bedingungen genutzt werden.</li>
          <li><strong>Prüfungen:</strong> Die App prüft den Schlüssel einmal bei der Aktivierung online und danach etwa einmal im Monat. Ohne Internet funktioniert Pro während einer Kulanzfrist weiter.</li>
          <li><strong>Kündigung:</strong> Kündige den Jahrestarif jederzeit in deinem PayPal-Konto. Pro bleibt bis zum Ende des bezahlten Zeitraums aktiv. Kündigst du in der Testphase, wird nichts abgebucht.</li>
          <li><strong>Erstattungen:</strong> volle Erstattung innerhalb von 14 Tagen nach jeder Zahlung, siehe <a href="/de/refund.html">Erstattungsrichtlinie</a>. Eine erstattete, zurückgebuchte oder angefochtene Zahlung deaktiviert den damit bezahlten Schlüssel.</li>
          <li><strong>Lebenslang:</strong> schaltet Pro frei, solange die App existiert und unterstützt wird.</li>
        </ul>

        ''',
    ),
)

LEGAL["es"] = dict(
    privacy=dict(
        updated="Última actualización: 10 de noviembre de 2026",
        collect='<p><strong>Nada desde la app.</strong> Watabook no tiene cuenta, ni inicio de sesión, ni analíticas, ni publicidad, ni seguimiento. No tenemos un servidor que guarde lo que introduces en la app.</p>\n        <p>La única excepción es comprar Pro en esta web: entonces guardamos un pequeño registro de licencia, descrito en <a href="#web-purchase">Si compras Pro en esta web</a> más abajo.</p>',
        license_li="<li><strong>Clave de licencia (Android, comprada en esta web):</strong> cuando introduces una clave, la app envía la clave y un identificador de dispositivo aleatorio creado por ella a nuestro servicio de licencias, una vez para activarla y después aproximadamente una vez al mes para comprobar que sigue siendo válida. La app no envía nombre, email ni ubicación.</li>",
        section=f'''<h2 id="web-purchase">Si compras Pro en esta web</h2>
        <p>Los pagos en esta web los procesa <strong>PayPal</strong>. Nunca vemos ni guardamos los datos de tu tarjeta o banco. Para darte una clave de licencia, nuestro servicio de licencias guarda:</p>
        <ul>
          <li>el email que PayPal nos facilita para tu compra, para enviarte la clave y ayudarte si la pierdes;</li>
          <li>tu clave de licencia, el plan, su fecha de caducidad y los ID de pedido o suscripción y de pago de PayPal;</li>
          <li>por cada dispositivo donde actives la clave: el identificador aleatorio del dispositivo, un nombre opcional y las fechas de activación y última comprobación.</li>
        </ul>
        <p>El servicio de licencias funciona en Cloudflare. Los emails con la clave se envían a través de Resend. Usamos tu email solo para tu clave y para dudas sobre tu compra, nunca para marketing salvo que lo aceptes por separado.</p>
        <p>Guardamos el registro de licencia mientras tu licencia sea válida y, después, el tiempo que exija la ley a efectos contables. Puedes pedir verlo o borrarlo en {MAIL}; borrarlo termina la licencia.</p>

        ''',
        control_li="<li>La app no guarda datos en nuestros servidores. Si compraste Pro en esta web, puedes pedir que borremos tu registro de licencia (ver arriba).</li>",
        children="<p>Watabook no está dirigido a niños. La app no recoge datos de nadie; las compras en esta web son para adultos con cuenta de PayPal o tarjeta.</p>",
    ),
    terms=dict(
        updated="Última actualización: 10 de noviembre de 2026",
        toc4="Suscripciones y compras",
        section4='''<h2 id="subscriptions">4. Suscripciones y compras</h2>
        <p>Watabook Pro se puede comprar de dos formas. Las reglas dependen de dónde lo compres.</p>
        <h3>En la App Store o en Google Play</h3>
        <p>Los pagos los procesan la App Store de Apple o Google Play, nunca nosotros directamente; no vemos ni guardamos tus datos de pago.</p>
        <ul>
          <li><strong>Prueba gratis:</strong> cuando se ofrece, una suscripción con renovación automática empieza con un periodo de prueba; si no cancelas antes de que termine, pasa a ser de pago automáticamente.</li>
          <li><strong>Renovación automática:</strong> las suscripciones se renuevan al precio mostrado en la compra hasta que canceles desde tu Apple ID o tu cuenta de Google Play.</li>
          <li><strong>De por vida:</strong> una compra única que desbloquea Pro mientras la App exista y siga recibiendo soporte, vinculada a tu Apple ID o cuenta de Google.</li>
          <li><strong>Reembolsos:</strong> los gestionan Apple o Google según sus propias políticas.</li>
          <li><strong>Restaurar compras:</strong> reinstalar la App o cambiar de dispositivo restaura tu derecho mediante tu Apple ID / cuenta de Google.</li>
        </ul>
        <h3>En esta web (Android), con PayPal</h3>
        <ul>
          <li><strong>Planes:</strong> Anual, con 7 días de prueba gratis y después renovación automática cada año al precio mostrado, o De por vida, con un solo pago. Precios en dólares estadounidenses. Los pagos los procesa PayPal; nunca vemos los datos de tu tarjeta o banco.</li>
          <li><strong>Clave de licencia:</strong> tras el pago recibes una clave por email y en la página. Una clave es para tu uso personal en hasta 3 dispositivos a la vez. Puedes liberar un dispositivo desde la app o con un enlace de restablecimiento enviado a tu email. No compartas ni vendas tu clave; podemos bloquear claves compartidas públicamente o usadas en contra de estos Términos.</li>
          <li><strong>Comprobaciones:</strong> la App comprueba la clave en línea una vez al activarla y después aproximadamente una vez al mes. Sin internet, Pro sigue funcionando durante un periodo de gracia.</li>
          <li><strong>Cancelación:</strong> cancela el plan anual cuando quieras en tu cuenta de PayPal. Pro sigue activo hasta el final del periodo pagado. Si cancelas durante la prueba gratis, no se cobra nada.</li>
          <li><strong>Reembolsos:</strong> reembolso completo en los 14 días siguientes a cualquier pago, consulta la <a href="/es/refund.html">Política de reembolso</a>. Un pago reembolsado, revertido o disputado desactiva la clave que pagó.</li>
          <li><strong>De por vida:</strong> desbloquea Pro mientras la App exista y siga recibiendo soporte.</li>
        </ul>

        ''',
    ),
)

LEGAL["pt"] = dict(
    privacy=dict(
        updated="Última atualização: 10 de novembro de 2026",
        collect='<p><strong>Nada a partir da app.</strong> O Watabook não tem conta, nem início de sessão, nem estatísticas, nem publicidade, nem rastreio. Não temos um servidor que guarde o que introduz na app.</p>\n        <p>A única exceção é comprar o Pro neste site: nesse caso guardamos um pequeno registo de licença, descrito em <a href="#web-purchase">Se comprar o Pro neste site</a> mais abaixo.</p>',
        license_li="<li><strong>Chave de licença (Android, comprada neste site):</strong> quando introduz uma chave, a app envia a chave e um identificador de dispositivo aleatório criado por ela para o nosso serviço de licenças, uma vez para ativar e depois cerca de uma vez por mês para verificar se continua válida. A app não envia nome, email nem localização.</li>",
        section=f'''<h2 id="web-purchase">Se comprar o Pro neste site</h2>
        <p>Os pagamentos neste site são processados pelo <strong>PayPal</strong>. Nunca vemos nem guardamos os dados do seu cartão ou banco. Para lhe dar uma chave de licença, o nosso serviço de licenças guarda:</p>
        <ul>
          <li>o email que o PayPal nos indica para a sua compra, para lhe enviar a chave e ajudar se a perder;</li>
          <li>a sua chave de licença, o plano, a data de validade e os ID de encomenda ou subscrição e de pagamento do PayPal;</li>
          <li>para cada dispositivo onde ativar a chave: o identificador aleatório do dispositivo, um nome opcional e as datas de ativação e da última verificação.</li>
        </ul>
        <p>O serviço de licenças funciona na Cloudflare. Os emails com a chave são enviados através da Resend. Usamos o seu email apenas para a chave e para dúvidas sobre a compra, nunca para marketing, salvo se aceitar separadamente.</p>
        <p>Guardamos o registo de licença enquanto a licença for válida e, depois, pelo tempo que a lei exigir para fins contabilísticos. Pode pedir para o consultar ou apagar em {MAIL}; apagá-lo termina a licença.</p>

        ''',
        control_li="<li>A app não guarda dados nos nossos servidores. Se comprou o Pro neste site, pode pedir que apaguemos o seu registo de licença (ver acima).</li>",
        children="<p>O Watabook não se destina a crianças. A app não recolhe dados de ninguém; as compras neste site destinam-se a adultos com conta PayPal ou cartão.</p>",
    ),
    terms=dict(
        updated="Última atualização: 10 de novembro de 2026",
        toc4="Subscrições e compras",
        section4='''<h2 id="subscriptions">4. Subscrições e compras</h2>
        <p>O Watabook Pro pode ser comprado de duas formas. As regras dependem de onde o compra.</p>
        <h3>Na App Store ou no Google Play</h3>
        <p>Os pagamentos são processados pela App Store da Apple ou pelo Google Play, nunca diretamente por nós; não vemos nem guardamos os seus dados de pagamento.</p>
        <ul>
          <li><strong>Teste grátis:</strong> quando oferecido, uma subscrição com renovação automática começa com um período de teste; se não cancelar antes do fim, passa automaticamente a paga.</li>
          <li><strong>Renovação automática:</strong> as subscrições renovam-se ao preço indicado na compra até cancelar através do seu Apple ID ou da conta Google Play.</li>
          <li><strong>Vitalício:</strong> uma compra única que desbloqueia o Pro enquanto a App existir e continuar a ser suportada, ligada ao seu Apple ID ou conta Google.</li>
          <li><strong>Reembolsos:</strong> tratados pela Apple ou pela Google segundo as suas próprias políticas.</li>
          <li><strong>Restaurar compras:</strong> reinstalar a App ou mudar de dispositivo restaura o seu direito através do Apple ID / conta Google.</li>
        </ul>
        <h3>Neste site (Android), com PayPal</h3>
        <ul>
          <li><strong>Planos:</strong> Anual, com 7 dias de teste grátis e depois renovação automática anual ao preço indicado, ou Vitalício, com um único pagamento. Preços em dólares americanos. Os pagamentos são processados pelo PayPal; nunca vemos os dados do seu cartão ou banco.</li>
          <li><strong>Chave de licença:</strong> após o pagamento recebe uma chave por email e na página. Uma chave é para uso pessoal em até 3 dispositivos ao mesmo tempo. Pode libertar um dispositivo na app ou com um link de reposição enviado para o seu email. Não partilhe nem venda a sua chave; podemos bloquear chaves partilhadas publicamente ou usadas contra estes Termos.</li>
          <li><strong>Verificações:</strong> a App verifica a chave online uma vez na ativação e depois cerca de uma vez por mês. Sem internet, o Pro continua a funcionar durante um período de tolerância.</li>
          <li><strong>Cancelamento:</strong> cancele o plano anual quando quiser na sua conta PayPal. O Pro mantém-se ativo até ao fim do período pago. Se cancelar durante o teste grátis, nada é cobrado.</li>
          <li><strong>Reembolsos:</strong> reembolso total nos 14 dias após qualquer pagamento, veja a <a href="/pt/refund.html">Política de reembolso</a>. Um pagamento reembolsado, revertido ou contestado desativa a chave que pagou.</li>
          <li><strong>Vitalício:</strong> desbloqueia o Pro enquanto a App existir e continuar a ser suportada.</li>
        </ul>

        ''',
    ),
)

LEGAL["it"] = dict(
    privacy=dict(
        updated="Ultimo aggiornamento: 10 novembre 2026",
        collect='<p><strong>Niente dall’app.</strong> Watabook non ha account, accesso, statistiche, pubblicità né tracciamento. Non abbiamo un server che conservi ciò che inserisci nell’app.</p>\n        <p>L’unica eccezione è l’acquisto di Pro su questo sito: in quel caso conserviamo un piccolo registro di licenza, descritto in <a href="#web-purchase">Se acquisti Pro su questo sito</a> qui sotto.</p>',
        license_li="<li><strong>Chiave di licenza (Android, acquistata su questo sito):</strong> quando inserisci una chiave, l’app invia la chiave e un identificativo casuale del dispositivo creato da lei al nostro servizio licenze, una volta per l’attivazione e poi circa una volta al mese per verificarne la validità. L’app non invia nome, email né posizione.</li>",
        section=f'''<h2 id="web-purchase">Se acquisti Pro su questo sito</h2>
        <p>I pagamenti su questo sito sono gestiti da <strong>PayPal</strong>. Non vediamo né conserviamo mai i dati della tua carta o del tuo conto. Per darti una chiave di licenza, il nostro servizio licenze conserva:</p>
        <ul>
          <li>l’indirizzo email che PayPal ci comunica per il tuo acquisto, per inviarti la chiave e aiutarti se la perdi;</li>
          <li>la chiave di licenza, il piano, la data di scadenza e gli ID PayPal di ordine o abbonamento e di pagamento;</li>
          <li>per ogni dispositivo su cui attivi la chiave: l’identificativo casuale del dispositivo, un nome facoltativo e le date di attivazione e dell’ultimo controllo.</li>
        </ul>
        <p>Il servizio licenze funziona su Cloudflare. Le email con la chiave sono inviate tramite Resend. Usiamo la tua email solo per la chiave e per domande sull’acquisto, mai per marketing salvo tuo consenso separato.</p>
        <p>Conserviamo il registro di licenza finché la licenza è valida e, dopo, per il tempo richiesto dalla legge ai fini contabili. Puoi chiedere di consultarlo o cancellarlo scrivendo a {MAIL}; la cancellazione termina la licenza.</p>

        ''',
        control_li="<li>L’app non conserva dati sui nostri server. Se hai acquistato Pro su questo sito, puoi chiedere la cancellazione del tuo registro di licenza (vedi sopra).</li>",
        children="<p>Watabook non è rivolto ai bambini. L’app non raccoglie dati da nessuno; gli acquisti su questo sito sono per adulti con account PayPal o carta.</p>",
    ),
    terms=dict(
        updated="Ultimo aggiornamento: 10 novembre 2026",
        toc4="Abbonamenti e acquisti",
        section4='''<h2 id="subscriptions">4. Abbonamenti e acquisti</h2>
        <p>Watabook Pro si può acquistare in due modi. Le regole dipendono da dove lo acquisti.</p>
        <h3>Sull’App Store o su Google Play</h3>
        <p>I pagamenti sono gestiti dall’App Store di Apple o da Google Play, mai direttamente da noi; non vediamo né conserviamo i tuoi dati di pagamento.</p>
        <ul>
          <li><strong>Prova gratuita:</strong> quando offerta, un abbonamento a rinnovo automatico inizia con un periodo di prova; se non disdici prima della fine, diventa automaticamente a pagamento.</li>
          <li><strong>Rinnovo automatico:</strong> gli abbonamenti si rinnovano al prezzo indicato all’acquisto finché non disdici tramite il tuo ID Apple o l’account Google Play.</li>
          <li><strong>A vita:</strong> un acquisto unico che sblocca Pro finché l’App esiste ed è supportata, legato al tuo ID Apple o account Google.</li>
          <li><strong>Rimborsi:</strong> gestiti da Apple o Google secondo le loro politiche.</li>
          <li><strong>Ripristino acquisti:</strong> reinstallare l’App o cambiare dispositivo ripristina il tuo diritto tramite ID Apple / account Google.</li>
        </ul>
        <h3>Su questo sito (Android), con PayPal</h3>
        <ul>
          <li><strong>Piani:</strong> Annuale, con 7 giorni di prova gratuita e poi rinnovo automatico ogni anno al prezzo indicato, oppure A vita, con un solo pagamento. Prezzi in dollari USA. I pagamenti sono gestiti da PayPal; non vediamo mai i dati della tua carta o del tuo conto.</li>
          <li><strong>Chiave di licenza:</strong> dopo il pagamento ricevi una chiave via email e nella pagina. Una chiave è per uso personale su un massimo di 3 dispositivi contemporaneamente. Puoi liberare un dispositivo dall’app o con un link di reset inviato alla tua email. Non condividere né vendere la tua chiave; possiamo bloccare le chiavi condivise pubblicamente o usate contro questi Termini.</li>
          <li><strong>Controlli:</strong> l’App verifica la chiave online una volta all’attivazione e poi circa una volta al mese. Senza internet, Pro continua a funzionare per un periodo di tolleranza.</li>
          <li><strong>Disdetta:</strong> disdici l’annuale quando vuoi dal tuo account PayPal. Pro resta attivo fino alla fine del periodo pagato. Se disdici durante la prova gratuita non viene addebitato nulla.</li>
          <li><strong>Rimborsi:</strong> rimborso completo entro 14 giorni da qualsiasi pagamento, vedi la <a href="/it/refund.html">Politica di rimborso</a>. Un pagamento rimborsato, stornato o contestato disattiva la chiave che ha pagato.</li>
          <li><strong>A vita:</strong> sblocca Pro finché l’App esiste ed è supportata.</li>
        </ul>

        ''',
    ),
)
