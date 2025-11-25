package game;

import game.screens.CharacterCreationScene;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Future Force - Juego Socioemocional");

        // Iniciar con la pantalla de creación de personaje
        CharacterCreationScene characterCreation = new CharacterCreationScene(primaryStage);

        Scene scene = new Scene(characterCreation.getRoot(), 900, 650);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
