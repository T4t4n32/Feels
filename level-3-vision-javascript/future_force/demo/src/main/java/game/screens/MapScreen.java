package game.screens;

import game.Player;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class MapScreen {

    private final Stage stage;
    private final Player player;

    public MapScreen(Stage stage, Player player) {
        this.stage = stage;
        this.player = player;
    }

    public void show() {

        Label title = new Label("MAPA DEL JUEGO");
        Label info = new Label("Jugador: " + player.getPlayerName());
        Label desc = new Label("Aquí irá el mapa exploratorio...");

        VBox root = new VBox(20, title, info, desc);
        root.setAlignment(Pos.CENTER);

        Scene scene = new Scene(root, 900, 600);
        stage.setScene(scene);
        stage.show();
    }
}
