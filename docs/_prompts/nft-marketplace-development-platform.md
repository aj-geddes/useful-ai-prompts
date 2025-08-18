---
category: blockchain
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
date: '2025-01-14'
description: This prompt helps you build comprehensive NFT marketplaces with minting, trading, royalties, and creator tools for digital art, collectibles, and tokenized assets.
layout: prompt
prompt: "-- Users table\nCREATE TABLE users (\n    id UUID PRIMARY KEY,\n    wallet_address VARCHAR(42) UNIQUE NOT NULL,\n    username VARCHAR(50) UNIQUE,\n    email VARCHAR(255),\n    profile_image_url TEXT,\n    verification_level INTEGER DEFAULT 0,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n\n-- NFT Collections\nCREATE TABLE collections (\n    id UUID PRIMARY KEY,\n    contract_address VARCHAR(42) NOT NULL,\n    creator_id UUID REFERENCES users(id),\n    name VARCHAR(255) NOT NULL,\n    description TEXT,\n    image_url TEXT,\n    royalty_percentage DECIMAL(5,2),\n    total_supply INTEGER,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n\n-- NFT Items\nCREATE TABLE nft_items (\n    id UUID PRIMARY KEY,\n    collection_id UUID REFERENCES collections(id),\n    token_id INTEGER NOT NULL,\n    name VARCHAR(255) NOT NULL,\n    description TEXT,\n    image_url TEXT NOT NULL,\n    metadata_url TEXT,\n    current_owner_id UUID REFERENCES users(id),\n    creator_id UUID REFERENCES users(id),\n    is_minted BOOLEAN DEFAULT FALSE,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n\n-- Marketplace Listings\nCREATE TABLE listings (\n    id UUID PRIMARY KEY,\n    nft_item_id UUID REFERENCES nft_items(id),\n    seller_id UUID REFERENCES users(id),\n    listing_type VARCHAR(20) NOT NULL, -- 'fixed', 'auction', 'offer'\n    price DECIMAL(20,8) NOT NULL,\n    currency VARCHAR(10) DEFAULT 'ETH',\n    start_time TIMESTAMP DEFAULT NOW(),\n    end_time TIMESTAMP,\n    is_active BOOLEAN DEFAULT TRUE,\n    created_at TIMESTAMP DEFAULT NOW()\n);"
related_prompts:
- smart-contract-security-audit-platform
- decentralized-finance-protocol-development
- blockchain-digital-identity-management-platform
slug: nft-marketplace-development-platform
tags:
- NFT marketplace
- digital collectibles
- art platform
- tokenization
- web3
title: NFT Marketplace Builder
use_cases:
- NFT marketplace development
- digital art platform
- collectibles trading
- creator monetization
version: 2.0.0
---
