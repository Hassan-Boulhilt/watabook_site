# Portuguese (pt-PT, matching the store listing). Legal pages are translations
# of the English originals; see the translation note at the end of privacy/terms.
L = dict(
    code="pt",
    htmllang="pt-PT",
    dir="ltr",
    nav=dict(
        main_aria="Navegação principal",
        home_aria="Página inicial do Watabook",
        features="Funcionalidades",
        pricing="Preços",
        privacy="Privacidade",
        terms="Termos",
        support="Apoio",
        download="Descarregar",
        menu_aria="Alternar navegação",
        language="Idioma",
        back="Voltar ao Watabook",
    ),
    index=dict(
        title="Watabook — Livro de manutenção e códigos de avaria",
        description="O Watabook é o livro de manutenção que também lhe diz o que está mal. Escreva ou fotografe um código de avaria e receba uma explicação em linguagem simples, além de lembretes de manutenção, controlo de combustível e despesas e um cofre de documentos. Offline, sem conta, sem anúncios.",
        keywords="luzes de aviso do carro, significado das luzes do painel, código de avaria, lembrete mudança de óleo, livro de manutenção do carro, controlo de manutenção, despesas do carro",
        og_title="Watabook — Livro de manutenção e códigos de avaria",
        og_desc="O livro de manutenção que também lhe diz o que está mal, em linguagem simples. Sem aparelho, sem conta, funciona totalmente offline.",
        tw_desc="O livro de manutenção que também lhe diz o que está mal, em linguagem simples. Offline, sem conta, sem anúncios.",
        ld_desc="Livro de manutenção do carro com dicionário offline de códigos de avaria OBD-II, referência das luzes do painel, lembretes de manutenção e controlo de custos.",
        kicker="Livro de manutenção e códigos de avaria",
        h1="O livro de manutenção que também lhe diz o que está mal.",
        lead="Sem aparelho. Sem conta. Funciona totalmente offline. Sem anúncios, nunca. Escreva ou fotografe um código de avaria e o Watabook explica-o em linguagem simples, além de um livro de manutenção completo, lembretes e o significado de 36 luzes do painel.",
        dl_on="Disponível na",
        get_on="Disponível no",
        free_note="<b>Grátis</b>: um veículo, entradas ilimitadas e o dicionário completo de códigos de avaria offline. O <b>Pro</b> acrescenta o resto, com 7 dias de teste.",
        phone=dict(
            title="Falha de ignição detetada no cilindro 1",
            body="Foi detetada uma falha de ignição no cilindro 1. Causas comuns: uma vela gasta, uma bobina de ignição avariada ou uma fuga de vácuo.",
            safe="Sem risco",
            gentle="À oficina",
            stop="Pare já",
            row1="Mudança de óleo — Clio",
            row1_sub="daqui a 900 km",
            row2="Inspeção periódica",
            row2_sub="até 12 mar 2027",
        ),
        sec_features="O que o Watabook faz",
        sec_pricing="Grátis vs. Pro",
        feats=[
            ("Perceber uma luz de aviso", "36 símbolos do painel explicados: vermelhos, âmbar, verdes e azuis, com o que significam e o que fazer. Escreva ou fotografe um código de avaria OBD-II e receba uma explicação em linguagem simples, um veredicto de &laquo;posso continuar a conduzir?&raquo;, causas prováveis e um intervalo de custo aproximado. O dicionário offline e todos os símbolos funcionam sem rede."),
            ("Não falhar uma revisão", "Mudança de óleo, filtros, líquido dos travões, pneus, correia de distribuição, renovação do seguro, inspeção periódica: lembre por data, por quilómetros ou pelo que chegar primeiro. Os lembretes recorrentes reagendam-se assim que os marca como feitos."),
            ("Um livro por carro", "Cada revisão, abastecimento, despesa e nota, com o conta-quilómetros, o custo e fotos. O consumo e o custo por quilómetro são calculados por si, para saber sempre quanto o seu carro custa mesmo, este ano e ao longo da vida."),
            ("Guardar os papéis", "Documento único, seguro e faturas, cifrados no seu telemóvel. Exporte tudo em CSV quando quiser: os seus dados nunca ficam presos."),
        ],
        free=dict(
            name="Grátis",
            price="&euro;0",
            sub="Sem conta. Sem anúncios, nunca.",
            items=[
                "1 veículo, entradas ilimitadas",
                "Lembretes por data e quilómetros",
                "Dicionário completo de códigos de avaria offline",
                "Significado de 36 luzes do painel",
                "Exportação CSV, quando quiser",
            ],
        ),
        pro=dict(
            badge="7 dias de teste",
            name="Watabook Pro",
            price="1,99&nbsp;&euro;",
            per_month="/mês",
            sub="ou 9,99&nbsp;&euro;/ano &middot; 19,99&nbsp;&euro; uma só vez, para sempre",
            items=[
                "Veículos ilimitados",
                "Respostas de IA &laquo;Explicar de forma simples&raquo; e voz",
                "Lembretes recorrentes inteligentes",
                "Cofre de documentos com alertas de validade",
                "PDF imprimível de manutenção e análises de custos",
            ],
        ),
        price_note="Preços em EUR &middot; a sua loja mostra o preço local &middot; cancele quando quiser.<br>As explicações com IA são informação geral, não um diagnóstico: mande sempre verificar por um profissional uma avaria crítica para a segurança.",
    ),
    privacy=dict(
        title="Política de privacidade — Watabook",
        description="Política de privacidade do Watabook. Tudo o que introduz fica no seu dispositivo: não há conta nem servidor que guarde os seus dados.",
        h1="Política de privacidade",
        updated="Última atualização: 12 de setembro de 2026",
        body="""        <p>O Watabook é um livro de manutenção para o seu carro. Foi criado para manter os seus dados <strong>no seu dispositivo</strong>.</p>

        <h2 id="collect">O que recolhemos</h2>
        <p><strong>Nada.</strong> O Watabook não tem conta, nem início de sessão, nem análise, nem publicidade, nem rastreamento. Não temos nenhum servidor que guarde as suas informações.</p>
        <p>Tudo o que introduz (veículos, entradas de manutenção e combustível, lembretes, documentos, histórico de códigos de avaria) é guardado apenas no armazenamento privado da app no seu telemóvel. Os documentos que adiciona ao cofre são cifrados no dispositivo.</p>

        <h2 id="internet">Quando a app usa a internet</h2>
        <p>O Watabook funciona totalmente offline. Só contacta a rede para as seguintes funcionalidades, e só quando as utiliza:</p>
        <ul>
          <li><strong>&laquo;Explicar de forma simples&raquo; (IA):</strong> envia o código de avaria, a marca do seu carro, o idioma escolhido e um identificador aleatório da app (não associado a si) ao nosso serviço de processamento, que pede ao Google Gemini uma explicação em linguagem simples. O seu nome, e-mail ou localização nunca são enviados.</li>
          <li><strong>Descodificação do VIN:</strong> envia o VIN de 17 carateres que escreve à base de dados pública de veículos da NHTSA dos EUA, para preencher a marca, o modelo e o ano.</li>
          <li><strong>Compras:</strong> a subscrição e a restauração são tratadas pela faturação da Apple / Google e pela RevenueCat, que recebe um comprovativo de compra e o seu próprio identificador anónimo, não a sua identidade.</li>
          <li><strong>Exportar e partilhar:</strong> quando exporta um CSV ou PDF, ou partilha um documento, o menu de partilha do seu dispositivo envia-o para onde <em>você</em> escolher. O Watabook não o transmite.</li>
        </ul>
        <p>Todas estas ligações usam HTTPS.</p>

        <h2 id="control">O seu controlo</h2>
        <ul>
          <li>Elimine qualquer entrada, documento ou veículo na app em qualquer momento.</li>
          <li>Desinstalar o Watabook remove permanentemente todos os seus dados do seu dispositivo.</li>
          <li>Não há dados em nenhum servidor para eliminar, porque não guardamos nenhuns.</li>
          <li>Exporte tudo em CSV quando quiser: os seus dados nunca ficam presos.</li>
        </ul>

        <h2 id="children">Crianças</h2>
        <p>O Watabook não se destina a crianças e não recolhe dados de ninguém.</p>

        <h2 id="changes">Alterações</h2>
        <p>Se esta política mudar, a data de &laquo;última atualização&raquo; acima será alterada e a nova versão será publicada aqui.</p>

        <h2 id="contact">Contacto</h2>
        <div class="contact-card">
          <div class="label">Questões de privacidade</div>
          <p>E-mail: <a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a></p>
        </div>

        <p><em>Esta é uma tradução do original em inglês. Em caso de divergência, prevalece a versão em inglês.</em></p>""",
    ),
    terms=dict(
        title="Termos de utilização — Watabook",
        description="Termos de utilização da app Watabook: subscrições, utilização aceitável, explicações com IA e aviso de segurança.",
        h1="Termos de utilização",
        effective="Em vigor desde: 12 de setembro de 2026",
        updated="Última atualização: 12 de setembro de 2026",
        body="""        <div class="note-box">
          <p>Leia estes Termos com atenção antes de usar o Watabook. Ao descarregar, instalar ou usar a app, aceita ficar vinculado por eles. Se não concordar, não use o Watabook.</p>
        </div>

        <div class="toc">
          <h3>Conteúdo</h3>
          <ol>
            <li><a href="#acceptance">Aceitação dos Termos</a></li>
            <li><a href="#description">Descrição do serviço</a></li>
            <li><a href="#your-data">Sem conta, os seus dados</a></li>
            <li><a href="#subscriptions">Subscrições e compras na app</a></li>
            <li><a href="#acceptable-use">Utilização aceitável</a></li>
            <li><a href="#disclaimer">Não é um diagnóstico: aviso de segurança</a></li>
            <li><a href="#third-party">Serviços de terceiros</a></li>
            <li><a href="#ip">Propriedade intelectual</a></li>
            <li><a href="#warranties">Exclusão de garantias</a></li>
            <li><a href="#liability">Limitação de responsabilidade</a></li>
            <li><a href="#termination">Cessação</a></li>
            <li><a href="#governing">Lei aplicável</a></li>
            <li><a href="#changes-terms">Alterações a estes Termos</a></li>
            <li><a href="#contact-terms">Contacto</a></li>
          </ol>
        </div>

        <h2 id="acceptance">1. Aceitação dos Termos</h2>
        <p>Estes Termos de utilização (&laquo;Termos&raquo;) constituem um acordo juridicamente vinculativo entre si (&laquo;você&raquo;, &laquo;Utilizador&raquo;) e a DevAndRepair (&laquo;nós&raquo;), o programador do Watabook, que rege o seu acesso e utilização da aplicação móvel Watabook (a &laquo;App&raquo;). Ao instalar ou usar a App, confirma que tem idade suficiente para aceitar estes Termos no seu país de residência e que leu, compreendeu e aceita estes Termos e a nossa <a href="/pt/privacy.html">Política de privacidade</a>.</p>

        <h2 id="description">2. Descrição do serviço</h2>
        <p>O Watabook é um livro de manutenção para o seu carro. Guarda os seus veículos, entradas de manutenção e combustível, lembretes e documentos localmente no seu dispositivo, e oferece um dicionário de consulta offline de códigos de avaria OBD-II e luzes do painel. Uma funcionalidade opcional, &laquo;Explicar de forma simples&raquo;, envia um código de avaria ao nosso serviço de processamento com IA para obter uma explicação em linguagem simples (ver §6 e §7).</p>
        <p>O Watabook é uma ferramenta de consulta e registo. Não é um instrumento de diagnóstico, não se liga ao seu veículo e não substitui a inspeção ou reparação por um mecânico qualificado.</p>

        <h2 id="your-data">3. Sem conta, os seus dados</h2>
        <ul>
          <li>O Watabook não tem conta nem início de sessão. Não há nada que possamos autenticar, suspender ou recuperar por si.</li>
          <li>Tudo o que introduz é guardado localmente no seu dispositivo, como descrito na nossa <a href="/pt/privacy.html">Política de privacidade</a>. Não temos qualquer cópia.</li>
          <li>É responsável pela segurança do seu próprio dispositivo (código de desbloqueio, cópias de segurança): perder ou repor o dispositivo sem cópia de segurança significa perder os seus dados do Watabook, pois não podemos restaurar o que nunca tivemos.</li>
          <li>Pode exportar tudo em CSV a qualquer momento, e desinstalar a App elimina permanentemente os seus dados do dispositivo.</li>
        </ul>

        <h2 id="subscriptions">4. Subscrições e compras na app</h2>
        <p>O Watabook Pro é oferecido como subscrição mensal ou anual com renovação automática, ou como compra única vitalícia. Todos os pagamentos são processados pela App Store da Apple ou pelo Google Play, nunca diretamente por nós: nunca vemos nem guardamos os seus dados de pagamento.</p>
        <ul>
          <li><strong>Teste gratuito:</strong> quando oferecido, uma subscrição com renovação automática começa com um período de teste gratuito; se não cancelar antes de terminar, converte-se automaticamente numa subscrição paga.</li>
          <li><strong>Renovação automática:</strong> as subscrições mensais e anuais renovam-se automaticamente ao preço apresentado na compra até que as cancele. Gira ou cancele uma subscrição nas definições do seu ID Apple ou da sua conta Google Play, não dentro da app, pois não temos um painel de faturação próprio.</li>
          <li><strong>Vitalícia:</strong> uma compra única que desbloqueia as funcionalidades Pro enquanto a App existir e continuar a ter suporte, associada ao seu ID Apple ou conta Google, não a uma conta Watabook (não existe).</li>
          <li><strong>Reembolsos:</strong> tratados integralmente pela Apple ou pelo Google, segundo as suas próprias políticas de reembolso. Não podemos emitir um reembolso diretamente.</li>
          <li><strong>Restaurar compras:</strong> ao reinstalar a App ou mudar de dispositivo, o seu direito é restaurado automaticamente através do seu ID Apple / conta Google, sem necessidade de iniciar sessão.</li>
        </ul>

        <h2 id="acceptable-use">5. Utilização aceitável</h2>
        <p>Compromete-se a não:</p>
        <ul>
          <li>fazer engenharia inversa, descompilar ou adulterar a App além do que os termos da sua plataforma permitem;</li>
          <li>usar a funcionalidade &laquo;Explicar de forma simples&raquo; para enviar algo que não seja um código de avaria OBD-II real e uma pergunta de seguimento de boa-fé;</li>
          <li>tentar contornar os limites de frequência, as verificações de direitos ou os limites da versão gratuita da App;</li>
          <li>usar a App para qualquer fim ilícito.</li>
        </ul>

        <h2 id="disclaimer">6. Não é um diagnóstico: aviso de segurança</h2>
        <div class="note-box">
          <p>Toda a explicação de um código de avaria, seja do dicionário offline integrado ou da funcionalidade de IA &laquo;Explicar de forma simples&raquo;, é <strong>informação geral, não um diagnóstico</strong>. Não inspeciona o seu veículo. Mande sempre verificar uma avaria crítica para a segurança por um mecânico qualificado antes de continuar a conduzir.</p>
        </div>
        <p>As causas prováveis, os intervalos de custo, a adequação a uma reparação por si e as indicações de &laquo;posso continuar a conduzir?&raquo; são estimativas destinadas a ajudá-lo a dar um passo seguinte sensato, não um substituto da inspeção profissional. O Watabook e a DevAndRepair não são responsáveis por qualquer decisão tomada, nem por danos, lesões ou perdas decorrentes de confiar nesta informação (ver §10).</p>

        <h2 id="third-party">7. Serviços de terceiros</h2>
        <p>A App depende de serviços que não controlamos, cada um regido pelos seus próprios termos:</p>
        <ul>
          <li>O dicionário offline de códigos de avaria baseia-se em dados do projeto de código aberto <a href="https://github.com/Wal33D/DTC-Database" target="_blank" rel="noopener">DTC-Database</a> (licença MIT), traduzidos automaticamente para os restantes idiomas da App.</li>
          <li>&laquo;Explicar de forma simples&raquo; é gerado pelo Google Gemini, chamado através do nosso próprio serviço de processamento: a App nunca detém diretamente uma chave de acesso.</li>
          <li>A descodificação do VIN usa a base de dados vPIC, gratuita e pública, da NHTSA dos EUA.</li>
          <li>As subscrições são faturadas pela Apple / Google e geridas através da RevenueCat.</li>
        </ul>
        <p>Não somos responsáveis pela disponibilidade ou exatidão destes serviços de terceiros.</p>

        <h2 id="ip">8. Propriedade intelectual</h2>
        <p>A app Watabook, o seu design e o seu conteúdo original pertencem à DevAndRepair. Não pode copiar, reproduzir ou criar obras derivadas da própria App. Mantém a plena propriedade dos dados que introduz (dados do veículo, notas, fotos, documentos); não reivindicamos quaisquer direitos sobre eles e, como nunca saem do seu dispositivo, não os poderíamos usar mesmo que quiséssemos.</p>

        <h2 id="warranties">9. Exclusão de garantias</h2>
        <p>A App é fornecida &laquo;tal como está&raquo; e &laquo;conforme disponível&raquo;, sem garantias de qualquer tipo, expressas ou implícitas, incluindo a adequação a um fim específico ou a não violação de direitos, na máxima medida permitida por lei.</p>

        <h2 id="liability">10. Limitação de responsabilidade</h2>
        <p>Na máxima medida permitida por lei, a responsabilidade total da DevAndRepair decorrente da sua utilização da App não excederá o montante que nos pagou nos 12 meses anteriores à reclamação, ou 20&nbsp;&euro;, consoante o que for maior. Não somos responsáveis por danos indiretos, acidentais ou consequenciais, incluindo os decorrentes de uma decisão de reparação de um veículo tomada com base em informação da App.</p>

        <h2 id="termination">11. Cessação</h2>
        <p>Pode deixar de usar a App e desinstalá-la em qualquer momento; ao fazê-lo, os seus dados locais são eliminados (ver §3). Podemos retirar a App da App Store ou do Google Play, ou descontinuar uma funcionalidade, a nosso critério; sempre que razoavelmente possível, daremos aviso através da ficha da loja ou desta página.</p>

        <h2 id="governing">12. Lei aplicável</h2>
        <p>Estes Termos regem-se pela lei da jurisdição em que a DevAndRepair opera, sem consideração pelas regras de conflitos de leis. Qualquer litígio será primeiro abordado através de negociação de boa-fé; se não for resolvido, será submetido aos tribunais competentes dessa jurisdição. Se uma disposição destes Termos for inexequível, as restantes permanecem em vigor.</p>

        <h2 id="changes-terms">13. Alterações a estes Termos</h2>
        <p>Podemos atualizar estes Termos de tempos a tempos. A data de &laquo;última atualização&raquo; acima será alterada e a nova versão será publicada aqui. Continuar a usar a App após uma alteração significa que aceita os Termos atualizados.</p>

        <h2 id="contact-terms">14. Contacto</h2>
        <div class="contact-card">
          <div class="label">Questões sobre os Termos</div>
          <p>E-mail: <a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a><br>
          Sítio web: <a href="https://watabook.devandrepair.com">watabook.devandrepair.com</a></p>
        </div>

        <p><em>Esta é uma tradução do original em inglês. Em caso de divergência, prevalece a versão em inglês.</em></p>""",
    ),
    support=dict(
        title="Apoio — Watabook",
        description="Apoio do Watabook: contacto e perguntas frequentes sobre utilização offline, subscrições, os seus dados e explicações com IA.",
        h1="Apoio",
        reply="Costumamos responder no prazo de 2 dias úteis.",
        body="""        <div class="contact-card">
          <div class="label">Fale connosco</div>
          <p>E-mail: <a href="mailto:hello@devandrepair.com">hello@devandrepair.com</a><br>
          Indique o seu dispositivo (iPhone/Android), a versão da app e o que aconteceu: uma captura de ecrã ajuda.</p>
        </div>

        <h2 id="faq">Perguntas frequentes</h2>

        <h3>Preciso de ligação à internet?</h3>
        <p>Não. O livro de manutenção, os lembretes, o cofre de documentos e todo o dicionário offline de códigos de avaria e luzes do painel funcionam sem qualquer rede. Só o &laquo;Explicar de forma simples&raquo; (IA) e o preenchimento automático do VIN precisam de ligação, e ambos continuam a funcionar de forma ordeira, sem erros, quando não há.</p>

        <h3>Cancelei o Pro: o que acontece aos meus dados?</h3>
        <p>Nada. O seu livro de manutenção, os lembretes e os documentos ficam exatamente como estão; a app volta apenas aos limites da versão gratuita (um veículo, um documento guardado). Nada é eliminado.</p>

        <h3>Como cancelo ou restauro uma subscrição?</h3>
        <p>As subscrições são faturadas pela Apple ou pelo Google, não por nós: pode geri-las, cancelá-las ou restaurá-las no seu ID Apple (Definições &rarr; o seu nome &rarr; Subscrições) ou no Google Play (Play Store &rarr; Menu &rarr; Pagamentos e subscrições).</p>

        <h3>Posso recuperar os meus dados se perder o telemóvel?</h3>
        <p>Apenas a partir da cópia de segurança do seu próprio dispositivo (iCloud / cópia de segurança Google): o Watabook não tem conta nem cópia num servidor, por conceção (veja a nossa <a href="/pt/privacy.html">Política de privacidade</a>). Exportar de vez em quando uma cópia em CSV é um bom hábito.</p>

        <h3>A explicação da IA é um diagnóstico real?</h3>
        <p>Não: é informação geral para o ajudar a compreender um código de avaria, nunca um substituto da inspeção de um mecânico. Veja os nossos <a href="/pt/terms.html#disclaimer">Termos, §6</a>.</p>""",
    ),
)
