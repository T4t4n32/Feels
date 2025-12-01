package game.screens;

import game.Player;
import javafx.geometry.Pos;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class gameMapScreen {

    private VBox root;

    public gameMapScreen(Stage stage, Player player) {

        root = new VBox(20);
        root.setAlignment(Pos.CENTER);
        root.setStyle("-fx-background-color: #101010;");

        Text title = new Text("Mapa del Juego");
        title.setFont(Font.font("Arial", 40));
        title.setFill(Color.WHITE);

        Text playerInfo = new Text("Jugador: " + player.getName() +
                "\nMentor: " + player.getMentor());
        playerInfo.setFont(Font.font("Arial", 22));
        playerInfo.setFill(Color.WHITE);

        Rectangle map = new Rectangle(500, 300, Color.GRAY);
        map.setArcWidth(25);
        map.setArcHeight(25);

        root.getChildren().addAll(title, playerInfo, map);
    }

    public VBox getRoot() {
        return root;
    }
}
