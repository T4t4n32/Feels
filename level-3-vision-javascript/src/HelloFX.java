import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class HelloFX extends Application {
    @Override
    public void start(Stage stage) {
        Label label = new Label("¡JavaFX 25 funcionando!");
        StackPane root = new StackPane(label);
        stage.setScene(new Scene(root, 300, 200));
        stage.setTitle("Prueba JavaFX");
        stage.show();
    }
    public static void main(String[] args) {
        launch(args);
    }
}
