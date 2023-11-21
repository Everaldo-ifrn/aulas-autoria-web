SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


CREATE SCHEMA IF NOT EXISTS `enapne` DEFAULT CHARACTER SET utf8 ;
USE `enapne` ;

-- -----------------------------------------------------
-- Table `enapne`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`curso` (
  `codigo` VARCHAR(6) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `coordenador` VARCHAR(100) NOT NULL,
  `campus` VARCHAR(50) NOT NULL,
  `nivelEnsino` VARCHAR(50) NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`aluno` (
  `matricula` VARCHAR(15) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `codigoCurso` VARCHAR(6) NOT NULL,
  `necessidadesEspecificas` VARCHAR(100) NULL,
  PRIMARY KEY (`matricula`),
  
  INDEX `fk_pertence_idx` (`codigoCurso` ASC) VISIBLE,
  CONSTRAINT `fk_pertence`
    FOREIGN KEY (`codigoCurso`)
    REFERENCES `enapne`.`curso` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`pei`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`pei` (
  `numero` VARCHAR(10) NOT NULL,
  `matriculaAluno` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`numero`),
  INDEX `fk_associa_idx` (`matriculaAluno` ASC) VISIBLE,
  CONSTRAINT `fk_associa`
    FOREIGN KEY (`matriculaAluno`)
    REFERENCES `enapne`.`aluno` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`equipeMultiDisciplinar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`equipeMultiDisciplinar` (
  `codigo` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `funcao` VARCHAR(100) NOT NULL,
  `numeroPei` VARCHAR(10) NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_multiPei_idx` (`numeroPei` ASC) VISIBLE,
  CONSTRAINT `fk_multiPei`
    FOREIGN KEY (`numeroPei`)
    REFERENCES `enapne`.`pei` (`numero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`anexo2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`anexo2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numeroPei` VARCHAR(10) NOT NULL,
  `disciplina` VARCHAR(50) NOT NULL,
  `docente` VARCHAR(50) NOT NULL,
  `objetivosPlanoDisciplina` TEXT NULL,
  `objetivosAdaptacoesDisciplina` TEXT NULL,
  `conteudoPlanoDisciplina` TEXT NULL,
  `conteudoAdaptacoesDisciplina` TEXT NULL,
  `metodologiaPlanoDisciplina` TEXT NULL,
  `metodologiaAdaptacoesDisciplina` TEXT NULL,
  `recursoDidaticoPlanoDisciplina` TEXT NULL,
  `recursoDidaticoAdaptacoesDisciplina` TEXT NULL,
  `avaliacaoPlanoDisciplina` TEXT NULL,
  `avaliacaoAdaptacoesDisciplina` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pertence2_idx` (`numeroPei` ASC) VISIBLE,
  CONSTRAINT `fk_pertence2`
    FOREIGN KEY (`numeroPei`)
    REFERENCES `enapne`.`pei` (`numero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`anexo3`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`anexo3` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numeroPei` VARCHAR(10) NOT NULL,
  `avancos` TEXT NULL,
  `parecer` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pertence3_idx` (`numeroPei` ASC) VISIBLE,
  CONSTRAINT `fk_pertence3`
    FOREIGN KEY (`numeroPei`)
    REFERENCES `enapne`.`pei` (`numero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`acompanhamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`acompanhamento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data` DATE NOT NULL,
  `descricao` TEXT NOT NULL,
  `idAnexo2` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_registros_idx` (`idAnexo2` ASC) VISIBLE,
  CONSTRAINT `fk_registros`
    FOREIGN KEY (`idAnexo2`)
    REFERENCES `enapne`.`anexo2` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`equipeNapne`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`equipeNapne` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `funcao` VARCHAR(100) NULL,
  `ativo` BINARY NULL,
  `usuario` VARCHAR(50) NULL,
  `senha` VARCHAR(256) NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enapne`.`anexo1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enapne`.`anexo1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numeroPei` VARCHAR(10) NOT NULL,
  `historico` TEXT NULL,
  `conhecimentosHabilidades` TEXT NULL,
  `dificuldades` TEXT NULL,
  `observacoes` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pertence1_idx` (`numeroPei` ASC) VISIBLE,
  CONSTRAINT `fk_pertence1`
    FOREIGN KEY (`numeroPei`)
    REFERENCES `enapne`.`pei` (`numero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;