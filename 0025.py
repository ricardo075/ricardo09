import streamlit as st
st.title('CALCULOS DE TEORIA DE CONJUNTO USANDO A FORMULA(A UNIAO B) #A+#B+#C-X (A INTERSEÇAO B) ')
def conjunto():
    n = st.number_input('Número total de pessoas(N):', min_value=0)
    a = st.number_input('Número de pessoas que fazem uma coisa(A):', min_value=0, max_value=n)
    b = st.number_input('Número de pessoas que fazem outra coisa(B):', min_value=0, max_value=n)
    c = st.number_input('Número de pessoas que fazem algumas coisas(C):', min_value=0, max_value=n)
    x = n - a + b
    # Cálculo da fórmula principal
    intersection = a + b + c - n

    # Cálculo de pessoas que fazem apenas uma coisa (A)
    a_only = a - intersection

    # Cálculo de pessoas que fazem outras coisas (B)
    b_only = b - intersection

    # Cálculo de pessoas que fazem algumas coisas (C)
    c_only = c - intersection

    # Apresentando os resultados
    st.write('DADOS:')
    st.write('NT: (NUMERO TOTAL)=', n)
    st.write('(A)numero que fazem apenas uma coisa=', a)
    st.write('(B): NUMERO DE PESSOAS QUE FAZEM OUTRAS COISAS=', b)
    st.write('(C): NUMERO DE PESSOAS QUE FAZEM ALGUMAS COISAS=', c)
    st.write('---')
    st.write('FORMULA')
    st.write('QUANDO TIVEREM OS :4: VALORES A FORMULA E /( #N = #A + #B + #C + X )/ E QUANDO SOMENTE TIVER :3: '
             'VALORES'
             'A FORMULA E /( #N = #A + #B - X )/')
    st.write('---')
    st.write('RESOLUÇAO')
    st.write('', n, '=', a, '+', b, '-X')
    st.write('', n, '=', a + b, '- X')
    st.write('', n, '-', a + b, '= - X')
    st.write('', n - a + b, '= - X')
    st.write('X =', n - a + b, )
    st.write('O número de pessoas que fazem as duas coisas é:', intersection)
    st.write('---')
    st.write('O número de pessoas que fazem apenas uma coisa (A) é:', a_only, ''
                                                                              'porque o valor de A=', a, 'que foi '
                                                                                                         ' subtraido'
                                                                                                 'pelo valor de X=',
             x, ';;(', a, '-', x, '=', a - x, )
    st.write('---')
    st.write('O número de pessoas que fazem outras coisas (B) é:', b_only, 'porque o valor de B=', b, 'foi subtraido'
                                                                                        ' pelo valor encontrado de X=',
             x, ';;(', b, '-', x, '=', b - x, )
    st.write('---')
    st.write('O número de pessoas que fazem algumas coisas (C) é:', c_only, ':: porque o valor de c=', c, ' que foi '
                                                                                                          'subtraido'
                                                                                     ' pelo valor encontrado de X=',
             x, ';;(', c, '-', x, '=', c - x, )
    st.write('---')
    st.write('O número de pessoas que fazem as duas coisas é:', intersection)
    st.write('O número de pessoas que fazem apenas uma coisa (A) é:', a_only)
    st.write('O número de pessoas que fazem outras coisas (B) é:', b_only)
    st.write('O número de pessoas que fazem algumas coisas (C) é:', c_only)

# Chamada da função para o site Streamlit
conjunto()
st.write('---')
st.write(
        'SE A PERGUNTA DO SEU CALCULO CONTER 4 VALORES,TOTAL,QUE FAZEM 1 COISA(A), OUTRA COISA(B),E ALGUMAS COISAS(C),'
        'PODE INSERIR O VALOR DE C, SE SO TIVER 3 VALORES INSIRA OS ATE O VALOR DE B E O VALOR DE C DEIXE NO 0,E TIRE '
        'SOMENTE O VALOR DE A E B DOS RESULTADOS')
st.write('---')
st.write('QUALQUER DUVIDA OU RECLAMAÇAO CONTACTE 868787572 OU 841038887')
st.write('CRATED BY RICARDO LIMA')
st.write('PROUCURANDO SEMPRE EVOLUIR')