********************************
Minerando Refactorings no GitHub
********************************
:date: 2014-11-24 20:38:16
:authors: Vagner Clementino
:category: Mestrado
:tags: UFMG, Mestrado, Software, Manutenção e Evolução
:slug: minerando-refactorings-no-github

O estudo dos padrões de refactorings vêm sendo bastante explorado na literatura. Contudo, no tocante à obtenção de seu dataset, a grande parte dos trabalhos focam nos `Sistemas de Controle de Versão (SCV) centralizados`_

Paralelo a isso, o `GitHub`_, que utiliza um SCV descentralizado, vêm nos últimos anos se apresentando como o principal repositório de software da Internet. Neste contexto, o presente trabalho propõe a analisar refactorings em projetos de código escrito em Java e hospedados no GitHub. Com base na análise de 4393 versões de sistema, pertencentes a 16 projetos, foi possı́vel detectar que:

    (i) o tipo de software afeta o padrão de refactorings
    (ii) e a atividade de refatoração é restrita a um pequeno grupo de desenvolvedores.

O estudo apresenta ainda uma nova abordagem para solucionar o problema do implicit branches que intrı́nseco à SCV descentralizados e pode causar a duplicidade de refactorings. O artigo completo detalhando o estudo pode ser obtido `aqui`_.

.. LINKS
.. _GitHub: http://github.com
.. _Sistemas de Controle de Versão (SCV) centralizados: https://en.wikipedia.org/wiki/Version_control
.. _aqui: {filename}/files/minerando-refactorings-github.pdf