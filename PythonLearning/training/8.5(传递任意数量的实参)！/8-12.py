def sandwichs(*materials):
    print('\nI am making the sandwich with below material for you')
    for material in materials:
        print('- ' + material.title())

sandwichs('egg')
sandwichs('egg','bacon')
sandwichs('egg','bacon','tomato')
