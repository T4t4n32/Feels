package game.screens;

import game.Player;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class CharacterCreationScene {

    private final Stage stage;
    private final VBox root;

    public CharacterCreationScene(Stage stage) {

        this.stage = stage;

        root = new VBox(20);
        root.setAlignment(Pos.CENTER);
        root.setStyle("-fx-background-color: #121212;");

        Text title = new Text("Crea tu personaje");
        title.setFont(Font.font("Arial", 40));
        title.setStyle("-fx-fill: white; -fx-font-weight: bold;");

        Label enterNameLabel = new Label("Ingresa tu nombre:");
        enterNameLabel.setStyle("-fx-text-fill: white; -fx-font-size: 18px;");

        TextField nameField = new TextField();
        nameField.setMaxWidth(300);
        nameField.setPromptText("Escribe tu nombre...");

        Label error = new Label();
        error.setStyle("-fx-text-fill: red; -fx-font-size: 14px;");

        Button continueBtn = new Button("Continuar");
        continueBtn.setStyle("-fx-font-size: 18px; -fx-padding: 10 20;");

        // Acción del botón
        continueBtn.setOnAction(e -> {
            String name = nameField.getText().trim();

            if (name.isEmpty()) {
                error.setText("El nombre no puede estar vacío.");
                return;
            }

            // Crear jugador
            Player player = new Player(name);

            // Ir a la pantalla de selección de mentor
            MentorSelectionScreen mentorScreen = new MentorSelectionScreen(stage, player);

            Scene nextScene = new Scene(mentorScreen.getRoot(), 900, 650);
            stage.setScene(nextScene);
            stage.show();
        });

        root.getChildren().addAll(title, enterNameLabel, nameField, error, continueBtn);
    }

    public VBox getRoot() {
        return root;
    }
}
