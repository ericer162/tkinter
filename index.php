<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ola PHP</title>
</head>
<body>
    <?php
        $saudacao = "Bem vindo";
        $nome_usuario = "Eric";
        $idade = 18;

        echo"$saudacao, $nome_usuario!";
        echo"<br>";
        echo"Voce tem " . $idade . "anos.";


        $hora_atual = date('H');

        if($hora_atual < 12) {
            echo "Bom dia!";
        } elseif ($hora_atual < 18){
            echo "Boa tarde!";
        } else {
            echo "Boa noite";
        }
    ?>
    <h1>Ola com PHP</h1>
    <p>A data de hoje é:  <?php  echo date("d/m/Y"); ?> </p>
    <p>Um numeno aleatorio entre 1 e 10: <?php echo rand(1, 10); ?></p>
</body>
</html>