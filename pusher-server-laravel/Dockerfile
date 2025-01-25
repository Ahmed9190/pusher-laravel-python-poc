# pusher-server-laravel/Dockerfile
FROM php:8.2-cli

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    libzip-dev \
    libonig-dev \
    libssl-dev \
    curl \
    && docker-php-ext-install pdo pdo_mysql zip mbstring sockets

# Install Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Copy application files
COPY . .

# Install dependencies (include --ignore-platform-reqs if needed)
RUN composer install --no-dev --optimize-autoloader --ignore-platform-reqs

# Set permissions
RUN chmod -R 777 storage bootstrap/cache

# Generate application key
RUN php artisan key:generate

# Expose port 9000 (default for php artisan serve)
EXPOSE 9000

# Start the Laravel development server
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=9000"]
