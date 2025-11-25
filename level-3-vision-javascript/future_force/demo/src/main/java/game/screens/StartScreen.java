package game.screens;

import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class StartScreen {

    private VBox root;

    public StartScreen(Stage stage) {

        root = new VBox(25);
        root.setAlignment(Pos.CENTER);
        root.setStyle("-fx-background-color: #1e1e1e;");

        Text title = new Text("Future Force");
        title.setFont(Font.font("Arial", 50));
        title.setStyle("-fx-fill: white; -fx-font-weight: bold;");

        Text subtitle = new Text("Forja tu futuro a través de tus decisiones");
        subtitle.setStyle("-fx-fill: white; -fx-font-size: 20px;");

        Button startBtn = new Button("Comenzar");
        startBtn.setStyle("-fx-font-size: 20px; -fx-padding: 10;");

        startBtn.setOnAction(e -> {
            CharacterCreationScene creation = new CharacterCreationScene(stage);
            Scene scene = new Scene(creation.getRoot(), 800, 600);
            stage.setScene(scene);
        });

        root.getChildren().addAll(title, subtitle, startBtn);
    }

    public VBox getRoot() {
        return root;
    }
}
