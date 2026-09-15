function calcular_desconto(preco, percentual=10){
    if(preco <= 0 || preco === null ){
        return None
    }

    const desconto = preco * (percentual / 100)
    return preco - desconto
}

calcular_desconto(1000)