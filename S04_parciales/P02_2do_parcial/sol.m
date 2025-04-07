df = load("..\..\S03_datasets\coactivation_matrix\Coactivation_matrix.mat");

maxK = 10; % Número máximo de clústeres a evaluar
wcss = zeros(maxK,1); % Vector para almacenar WCSS

% Aplicar k-means para diferentes valores de k
for k = 1:maxK
    [~,~,sumd] = kmeans(df.Coactivation_matrix, k);
    disp(sumd)
    wcss(k) = sum(sumd(:)); % Guardar WCSS
end

% Graficar el método del codo
figure;
plot(1:maxK, wcss, '-o', 'LineWidth', 2);
xlabel('Número de Clusters (k)');
ylabel('Suma de los Errores Cuadráticos (WCSS)');
title('Método del Codo para Seleccionar k');
grid on;


[idx, C] = kmeans(df.Coactivation_matrix,5);
scatter3(df.Coord(:, 1), df.Coord(:, 2), df.Coord(:, 3), 20, idx, 'filled')