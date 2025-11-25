package game.screens;

import game.Player;
import game.models.Mentor;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class MentorSelectionScreen {

    private final VBox root;
    private final Stage stage;
    private final Player player;

    public MentorSelectionScreen(Stage stage, Player player) {
        this.stage = stage;
        this.player = player;

        root = new VBox(30);
        root.setAlignment(Pos.CENTER);
        root.setStyle("-fx-background-color: #202020; -fx-padding: 20;");

        Text title = new Text("Elige tu Mentor");
        title.setFont(Font.font("Arial", 40));
        title.setStyle("-fx-fill: white; -fx-font-weight: bold;");

        // Crear los mentores
        Mentor sofia = new Mentor(
                "Sofía Rivera",
                "Científica Estratega",
                "Combinación de paciencia metódica y rigor científico.\n" +
                        "Guía hacia caminos de investigación, disciplina y visión a largo plazo."
        );

        Mentor leo = new Mentor(
                "Leo 'El Fénix' Márquez",
                "Carisma e Impulso",
                "Experto en decisiones rápidas y comunicativas.\n" +
                        "Ayuda a identificar riesgos y presiones sociales."
        );

        Mentor costa = new Mentor(
                "Profesor Costa",
                "Advertencia Brillante",
                "Un genio que aprendió del fracaso y ahora enseña con honestidad.\n" +
                        "Guía para evitar caminos impulsivos o sin visión."
        );

        HBox mentorsBox = new HBox(25);
        mentorsBox.setAlignment(Pos.CENTER);

        mentorsBox.getChildren().addAll(
                createMentorCard(sofia),
                createMentorCard(leo),
                createMentorCard(costa)
        );

        root.getChildren().addAll(title, mentorsBox);
    }

    private VBox createMentorCard(Mentor mentor) {

        Text name = new Text(mentor.getNombre());
        name.setStyle("-fx-fill: white; -fx-font-size: 22px; -fx-font-weight: bold;");

        TextArea description = new TextArea(mentor.getDescripcion());
        description.setEditable(false);
        description.setWrapText(true);
        description.setPrefSize(200, 150);

        Button selectButton = new Button("Seleccionar");
        selectButton.setStyle("-fx-font-size: 18px;");
        selectButton.setOnAction(e -> {
            System.out.println("Mentor seleccionado: " + mentor.getNombre());

            // Ir a mapa
            MapScreen mapScreen = new MapScreen(stage, player);
            mapScreen.show();
        });

        VBox card = new VBox(10, name, description, selectButton);
        card.setAlignment(Pos.CENTER);
        card.setStyle("-fx-background-color: #333333; -fx-padding: 15; -fx-border-color: white;");

        return card;
    }

    public VBox getRoot() {
        return root;
    }
}
